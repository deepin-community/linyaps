// SPDX-FileCopyrightText: 2024 UnionTech Software Technology Co., Ltd.
//
// SPDX-License-Identifier: LGPL-3.0-or-later

#pragma once

#include "linglong/api/types/v1/PackageInfo.hpp"
#include "linglong/api/types/v1/PackageInfoV2.hpp"
#include "linglong/utils/error/error.h"

#include <gio/gio.h>

#include <QString>

#define PACKAGE_INFO_VERSION "1.0"

namespace linglong::utils {

api::types::v1::PackageInfoV2 toPackageInfoV2(const api::types::v1::PackageInfo &oldInfo);
error::Result<api::types::v1::PackageInfoV2> parsePackageInfo(const QString &path);
error::Result<api::types::v1::PackageInfoV2> parsePackageInfo(const nlohmann::json &json);
error::Result<api::types::v1::PackageInfoV2> parsePackageInfo(GFile *file);
}; // namespace linglong::utils
