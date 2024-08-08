/**
 * linglong仓库
 * 玲珑仓库接口
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: wurongjie@deepin.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * Request_FuzzySearchReq.h
 *
 * 
 */

#ifndef Request_FuzzySearchReq_H
#define Request_FuzzySearchReq_H

#include <QJsonObject>

#include <QString>

#include "Enum.h"
#include "Object.h"

namespace linglong {
namespace api {
namespace client {

class Request_FuzzySearchReq : public Object {
public:
    Request_FuzzySearchReq();
    Request_FuzzySearchReq(QString json);
    ~Request_FuzzySearchReq() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getChannel() const;
    void setChannel(const QString &channel);
    bool is_channel_Set() const;
    bool is_channel_Valid() const;

    QString getAppId() const;
    void setAppId(const QString &app_id);
    bool is_app_id_Set() const;
    bool is_app_id_Valid() const;

    QString getArch() const;
    void setArch(const QString &arch);
    bool is_arch_Set() const;
    bool is_arch_Valid() const;

    QString getRepoName() const;
    void setRepoName(const QString &repo_name);
    bool is_repo_name_Set() const;
    bool is_repo_name_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_channel;
    bool m_channel_isSet;
    bool m_channel_isValid;

    QString m_app_id;
    bool m_app_id_isSet;
    bool m_app_id_isValid;

    QString m_arch;
    bool m_arch_isSet;
    bool m_arch_isValid;

    QString m_repo_name;
    bool m_repo_name_isSet;
    bool m_repo_name_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace linglong
} // namespace api
} // namespace client

Q_DECLARE_METATYPE(linglong::api::client::Request_FuzzySearchReq)

#endif // Request_FuzzySearchReq_H