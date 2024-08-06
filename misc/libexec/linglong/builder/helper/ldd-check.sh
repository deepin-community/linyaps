#!/bin/bash

# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

#ldd check binary script

declare failedList
declare -i total=0 pass=0 fail=0

if [ "$1" == "" ]; then
        echo "usage: lddscan.sh path or lddscan.sh [path1:path2:pathn]"
        exit -1
fi

#support multiple path, split by ':'
paths=$(echo $1 | tr ':' ' ')

filePaths=$(find $paths -type f)
IFS=$'\n'
for filePath in $filePaths; do
        mimeType=$(file $filePath --mime-type)
        isPieExe=$(echo $mimeType | grep "application/x-pie-executable")
        isSharedLib=$(echo $mimeType | grep "application/x-sharedlib")
        if [[ "$isPieExe" != "" || "$isSharedLib" != "" ]]; then
                echo "$filePath is ELF, checking ..."
                total+=1
                if [ "$(ldd $filePath | grep "not found")" != "" ]; then
                        echo "Warning! The ldd check is failed: $filePath"
                        fail+=1
                        failedList+="$filePath\n"
                        continue
                fi

                if [[ ${elementSize} -eq 2 ]]; then
                        # https://regex101.com/r/sPAsBt/1
                        # https://man7.org/linux/man-pages/man7/vdso.7.html
                        if [[ ${elements[0]:0:1} == "/" ]]; then
                                dependLibs+=("$(realpath "${elements[0]}")")
                        elif [[ ${elements[0]} =~ linux-(vdso|gate){1}(32|64)?\.so\.[0-9]+ ]]; then
                                continue
                                #ignore virtual ELF dynamic shared object
                        else
                                rawStr="${elements[0]} ${elements[1]}"
                                if [[ ${rawStr} == "statically linked" ]]; then
                                        continue
                                fi
                                logErr "unexpected conditions, unkonwn line: ${line}"
                        fi
                elif [[ ${elementSize} -eq 4 ]]; then
                        rawStr="${elements[2]} ${elements[3]}"
                        if [[ ${rawStr} == "not found" ]]; then
                                logErr "couldn't find dependency \"${elements[0]}\" of ${filePath}"
                                continue
                        fi

                        # clean path
                        dependLibs+=("$(realpath "${elements[2]}")")
                else
                        logErr "unexpected conditions, unkonwn line: ${line}"
                fi
        done
}

updateDepensLibs() {
        #support multiple path, split by ':'
        declare paths
        paths=$(echo "$1" | tr ':' ' ')

        if [[ -z ${paths} ]]; then
                logErr "No paths provided"
                return 255
        fi
done

        filePaths=$(find "${paths}" -type f)

        IFS=$'\n'
        for filePath in ${filePaths}; do
                local mimeType
                mimeType="$(file --mime-type --brief "${filePath}")"
                if [[ ${mimeType} == "application/x-pie-executable" ]]; then
                        processExecBin "${filePath}"
                fi
        done

        # remove duplicates
        local oldIFS="${IFS}"
        IFS=" " read -r -a dependLibs <<<"$(echo "${dependLibs[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' ' || true)"
        IFS="${oldIFS}"
}

element_in_array() {
        local element="$1"
        shift
        local array=("$@")
        for item in "${array[@]}"; do
                if [[ ${item} == "${element}" ]]; then
                        return 0
                fi
        done
        return 1
}

main() {
        declare arg1="$1"
        if [[ -z ${arg1} ]]; then
                echo "usage:
                        ldd-check.sh path
                        ldd-check.sh [path:...]"
                return 0
        fi

        logDbg "start checking..."

        # Get the needed dynamic libraries for the specified binaries
        updateDepensLibs "${arg1}"

        # Get all dynamic libraries
        readarray -t allLibs <<<"$(ldconfig -p | awk 'NR>2 {print last} {last=$4}' | xargs realpath | sort -u || true)"

        dependLibsContent=$(printf "%s\n" "${dependLibs[@]}" | sort -u)
        local tailorableList=()
        for item in "${allLibs[@]}"; do
                if [[ -z "$(echo "${dependLibsContent}" | grep "${item}" || true)" ]]; then
                        tailorableList+=("${item}")
                fi
        done

        yamlContent="# Attention: the content of this file and the file name\n"
        yamlContent+="# is linglong internal infomation, please DO NOT use\n"
        yamlContent+="# these contents in other places. The content may be\n"
        yamlContent+="# different in the future.\n\n"
        yamlContent+="# Usage: Comment which library you want to keep in uab\n\n"
        yamlContent+="extra_libs:\n"
        yamlContent+=$(printf "  - %s\n" "${tailorableList[@]}")
        echo -e "${yamlContent}" >"/project/extraLibs.uab.yaml"

        logDbg "checking done"
        return 0
}

set -eo pipefail
main "$@"
