/*
 * SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
 *
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

#ifndef LINGLONG_API_V1_DBUS_PACKAGEMANAGER1_H_
#define LINGLONG_API_V1_DBUS_PACKAGEMANAGER1_H_

#include "linglong/api/dbus/v1/gen_org_deepin_linglong_packagemanager1.h"

namespace linglong::api::dbus::v1 {

class PackageManager : public ::OrgDeepinLinglongPackageManager1Interface
{
public:

    using OrgDeepinLinglongPackageManager1Interface::OrgDeepinLinglongPackageManager1Interface;
    enum class Operation : uint16_t { Add, Remove, Update, Use, Unknown };
};

} // namespace linglong::api::dbus::v1

#endif
