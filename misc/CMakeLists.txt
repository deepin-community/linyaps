# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

include(GNUInstallDirs)

function(configure_files)
  foreach(input ${ARGV})
    configure_file(${input} ${input} @ONLY)
  endforeach()
endfunction()

configure_files(
  # find -regex '\.\/\(script\|share\|lib\|libexec\)\/.*' -type f -printf '%P\n'
  # | sort
  libexec/linglong/app-conf-generator
  libexec/linglong/builder/helper/config-check.sh
  libexec/linglong/builder/helper/ldd-check.sh
  libexec/linglong/builder/helper/main-check.sh
  libexec/linglong/builder/helper/symbols-strip.sh
  libexec/linglong/dialog/99-linglong-permission
  libexec/linglong/fetch-archive-source
  libexec/linglong/fetch-dsc-source
  libexec/linglong/fetch-file-source
  libexec/linglong/fetch-git-source
  libexec/linglong/font-cache-generator
  libexec/linglong/ld-cache-generator
  lib/linglong/container/config.d/00-id-mapping
  lib/linglong/container/config.d/05-initialize
  lib/linglong/container/config.d/10-basics.json
  lib/linglong/container/config.d/20-devices
  lib/linglong/container/config.d/25-host-env
  lib/linglong/container/config.d/25-host-rootfs.json
  lib/linglong/container/config.d/25-host-statics.json
  lib/linglong/container/config.d/30-user-home
  lib/linglong/container/config.d/40-host-ipc
  lib/linglong/container/config.d/90-legacy
  lib/linglong/container/config.json
  lib/linglong/container/README.md
  lib/linglong/generate-xdg-data-dirs.sh
  lib/systemd/system-environment-generators/61-linglong
  lib/systemd/system/org.deepin.linglong.PackageManager.service
  lib/systemd/system-preset/91-linglong.preset
  lib/systemd/user-generators/linglong-user-systemd-generator
  lib/systemd/user/linglong-session-helper.service
  lib/sysusers.d/linglong.conf
  lib/tmpfiles.d/linglong.conf
  script/linglong.sh
  share/bash-completion/completions/ll-builder
  share/bash-completion/completions/ll-cli
  share/zsh/vendor-completions/_ll-cli
  share/dbus-1/system.d/org.deepin.linglong.PackageManager1.conf
  share/dbus-1/system-services/org.deepin.linglong.PackageManager1.service
  share/linglong/export-dirs.json
  share/linglong/builder/templates/example.yaml
  share/linglong/builder/uab/blacklist
  share/linglong/config.yaml
  share/mime/packages/vnd.linyaps.uab.xml
  share/polkit-1/actions/org.deepin.linglong.PackageManager1.policy
  share/applications/linyaps.desktop)

# bash-completion
set(BASH_COMPLETIONS_DIR ${CMAKE_INSTALL_DATADIR}/bash-completion)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/share/bash-completion/completions
        DESTINATION ${BASH_COMPLETIONS_DIR})

# zsh-completion
set(ZSH_COMPLETIONS_DIR ${CMAKE_INSTALL_DATADIR}/zsh)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/share/zsh/vendor-completions
        DESTINATION ${ZSH_COMPLETIONS_DIR})

# dbus
set(DBUS_SYSTEM_BUS_DIR ${CMAKE_INSTALL_DATADIR}/dbus-1)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/share/dbus-1/system.d
        DESTINATION ${DBUS_SYSTEM_BUS_DIR})
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/share/dbus-1/system-services
        DESTINATION ${DBUS_SYSTEM_BUS_DIR})

# libexec
set(LIBEXEC_LINGLONG_DIR ${CMAKE_INSTALL_PREFIX}/libexec/linglong)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/app-conf-generator
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/ld-cache-generator
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/font-cache-generator
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/fetch-archive-source
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/fetch-dsc-source
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/fetch-file-source
           ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/fetch-git-source
  DESTINATION ${LIBEXEC_LINGLONG_DIR})

set(LINGLONG_DIALOG_DIR ${LIBEXEC_LINGLONG_DIR}/dialog)
install(
  PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/dialog/99-linglong-permission
  DESTINATION ${LINGLONG_DIALOG_DIR})

# builder helpers
set(LIBEXEC_LINGLONG_BUILDER_DIR ${LIBEXEC_LINGLONG_DIR}/builder)
install(
  PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/builder/helper/config-check.sh
    ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/builder/helper/ldd-check.sh
    ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/builder/helper/main-check.sh
    ${CMAKE_CURRENT_BINARY_DIR}/libexec/linglong/builder/helper/symbols-strip.sh
  DESTINATION ${LIBEXEC_LINGLONG_BUILDER_DIR}/helper)

# linglong
set(LINGLONG_CONFIG_DIR
    ${CMAKE_CURRENT_BINARY_DIR}/lib/linglong/container/config.d)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/lib/linglong/generate-xdg-data-dirs.sh
  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/linglong)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/lib/linglong/container/config.json
              ${CMAKE_CURRENT_BINARY_DIR}/lib/linglong/container/README.md
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/linglong/container)

install(
  FILES ${LINGLONG_CONFIG_DIR}/10-basics.json
        ${LINGLONG_CONFIG_DIR}/25-host-rootfs.json
        ${LINGLONG_CONFIG_DIR}/25-host-statics.json
        ${LINGLONG_CONFIG_DIR}/00-id-mapping
        ${LINGLONG_CONFIG_DIR}/05-initialize
        ${LINGLONG_CONFIG_DIR}/20-devices
        ${LINGLONG_CONFIG_DIR}/25-host-env
        ${LINGLONG_CONFIG_DIR}/30-user-home
        ${LINGLONG_CONFIG_DIR}/40-host-ipc
        ${LINGLONG_CONFIG_DIR}/90-legacy
  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/linglong/container/config.d)

# linglong default configuration
install(FILES ${CMAKE_CURRENT_LIST_DIR}/share/linglong/config.yaml
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/linglong)

# builder export dirs
install(FILES ${CMAKE_CURRENT_LIST_DIR}/share/linglong/export-dirs.json
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/linglong)

# builder templates
install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/share/linglong/builder/templates/
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/linglong/builder/templates)
install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/share/linglong/builder/uab/
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/linglong/builder/uab)

# systemd
set(SYSTEMD_SYSTEM_PRESET_PATH
    ${CMAKE_INSTALL_PREFIX}/lib/systemd/system-preset)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/systemd/system-preset/
        DESTINATION ${SYSTEMD_SYSTEM_PRESET_PATH})

set(SYSTEMD_SYSTEM_UNIT_PATH ${CMAKE_INSTALL_PREFIX}/lib/systemd)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/systemd/system
        DESTINATION ${SYSTEMD_SYSTEM_UNIT_PATH})

set(SYSTEMD_USER_UNIT_PATH ${CMAKE_INSTALL_PREFIX}/lib/systemd)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/systemd/user
        DESTINATION ${SYSTEMD_USER_UNIT_PATH})

set(SYSTEMD_SYSTEM_GENERATOR_PATH
    ${CMAKE_INSTALL_PREFIX}/lib/systemd/system-environment-generators)

install(
  PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/lib/systemd/system-environment-generators/61-linglong
  DESTINATION ${SYSTEMD_SYSTEM_GENERATOR_PATH})

install(
  PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/lib/systemd/user-generators/linglong-user-systemd-generator
  DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/systemd/user-generators)

# sysuser

set(SYSTEMD_SYSUSERSDIR ${CMAKE_INSTALL_PREFIX}/lib/sysusers.d)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/sysusers.d/
        DESTINATION ${SYSTEMD_SYSUSERSDIR})

# tmpfiles
set(SYSTEMD_TMPFILESDIR ${CMAKE_INSTALL_PREFIX}/lib/tmpfiles.d)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/tmpfiles.d/
        DESTINATION ${SYSTEMD_TMPFILESDIR})

# xdg
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/share/mime/packages
        DESTINATION ${CMAKE_INSTALL_DATADIR}/mime)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/share/applications/linyaps.desktop
        DESTINATION ${CMAKE_INSTALL_DATADIR}/applications)

# set linglong XDG_DATA_DIRS environtment
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/script/linglong.sh
        DESTINATION /etc/profile.d)

install(
  FILES ${CMAKE_CURRENT_BINARY_DIR}/script/linglong.sh
  DESTINATION /etc/X11/Xsession.d/
  RENAME 21linglong)

# polkit actions
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/share/polkit-1/actions/org.deepin.linglong.PackageManager1.policy
  DESTINATION ${CMAKE_INSTALL_DATADIR}/polkit-1/actions)
