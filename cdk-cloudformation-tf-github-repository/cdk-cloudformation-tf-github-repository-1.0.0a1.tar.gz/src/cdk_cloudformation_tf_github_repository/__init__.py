'''
# AWS CDK CloudFormation Constructs for TF::GitHub::Repository

This resource allows you to create and manage repositories within your
GitHub organization or personal account.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/github/TF-GitHub-Repository/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


class CfnRepository(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-github-repository.CfnRepository",
):
    '''A CloudFormation ``TF::GitHub::Repository``.

    :cloudformationResource: TF::GitHub::Repository
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        allow_merge_commit: typing.Optional[builtins.bool] = None,
        allow_rebase_merge: typing.Optional[builtins.bool] = None,
        allow_squash_merge: typing.Optional[builtins.bool] = None,
        archived: typing.Optional[builtins.bool] = None,
        archive_on_destroy: typing.Optional[builtins.bool] = None,
        auto_init: typing.Optional[builtins.bool] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[builtins.bool] = None,
        has_issues: typing.Optional[builtins.bool] = None,
        has_projects: typing.Optional[builtins.bool] = None,
        has_wiki: typing.Optional[builtins.bool] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[builtins.bool] = None,
        license_template: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Sequence["PagesDefinition"]] = None,
        private: typing.Optional[builtins.bool] = None,
        template: typing.Optional[typing.Sequence["TemplateDefinition"]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``TF::GitHub::Repository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the repository.
        :param allow_merge_commit: Set to ``false`` to disable merge commits on the repository.
        :param allow_rebase_merge: Set to ``false`` to disable rebase merges on the repository.
        :param allow_squash_merge: Set to ``false`` to disable squash merges on the repository.
        :param archived: Specifies if the repository should be archived. Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving. Default: false`. **NOTE** Currently, the API does not support unarchiving.
        :param archive_on_destroy: Set to ``true`` to archive the repository instead of deleting on destroy.
        :param auto_init: Set to ``true`` to produce an initial commit in the repository.
        :param default_branch: (Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created, and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the initial repository creation and create the target branch inside of the repository prior to setting this attribute.
        :param delete_branch_on_merge: Automatically delete head branch after a pull request is merged. Defaults to ``false``. Default: false`.
        :param description: A description of the repository.
        :param gitignore_template: Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".
        :param has_downloads: Set to ``true`` to enable the (deprecated) downloads features on the repository.
        :param has_issues: Set to ``true`` to enable the GitHub Issues features on the repository.
        :param has_projects: Set to ``true`` to enable the GitHub Projects features on the repository. Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.
        :param has_wiki: Set to ``true`` to enable the GitHub Wiki features on the repository.
        :param homepage_url: URL of a page describing the project.
        :param is_template: Set to ``true`` to tell GitHub that this is a template repository.
        :param license_template: Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".
        :param pages: 
        :param private: Set to ``true`` to create a private repository. Repositories are created as public (e.g. open source) by default.
        :param template: 
        :param topics: The list of topics of the repository.
        :param visibility: Can be ``public`` or ``private``. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.
        :param vulnerability_alerts: 
        '''
        props = CfnRepositoryProps(
            name=name,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            archive_on_destroy=archive_on_destroy,
            auto_init=auto_init,
            default_branch=default_branch,
            delete_branch_on_merge=delete_branch_on_merge,
            description=description,
            gitignore_template=gitignore_template,
            has_downloads=has_downloads,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            homepage_url=homepage_url,
            is_template=is_template,
            license_template=license_template,
            pages=pages,
            private=private,
            template=template,
            topics=topics,
            visibility=visibility,
            vulnerability_alerts=vulnerability_alerts,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEtag")
    def attr_etag(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.Etag``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEtag"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFullName")
    def attr_full_name(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.FullName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFullName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrGitCloneUrl")
    def attr_git_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.GitCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGitCloneUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHtmlUrl")
    def attr_html_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.HtmlUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHtmlUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHttpCloneUrl")
    def attr_http_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.HttpCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHttpCloneUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNodeId")
    def attr_node_id(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.NodeId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNodeId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRepoId")
    def attr_repo_id(self) -> jsii.Number:
        '''Attribute ``TF::GitHub::Repository.RepoId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRepoId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSshCloneUrl")
    def attr_ssh_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.SshCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshCloneUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSvnUrl")
    def attr_svn_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.SvnUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSvnUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnRepositoryProps":
        '''Resource props.'''
        return typing.cast("CfnRepositoryProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allow_merge_commit": "allowMergeCommit",
        "allow_rebase_merge": "allowRebaseMerge",
        "allow_squash_merge": "allowSquashMerge",
        "archived": "archived",
        "archive_on_destroy": "archiveOnDestroy",
        "auto_init": "autoInit",
        "default_branch": "defaultBranch",
        "delete_branch_on_merge": "deleteBranchOnMerge",
        "description": "description",
        "gitignore_template": "gitignoreTemplate",
        "has_downloads": "hasDownloads",
        "has_issues": "hasIssues",
        "has_projects": "hasProjects",
        "has_wiki": "hasWiki",
        "homepage_url": "homepageUrl",
        "is_template": "isTemplate",
        "license_template": "licenseTemplate",
        "pages": "pages",
        "private": "private",
        "template": "template",
        "topics": "topics",
        "visibility": "visibility",
        "vulnerability_alerts": "vulnerabilityAlerts",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        allow_merge_commit: typing.Optional[builtins.bool] = None,
        allow_rebase_merge: typing.Optional[builtins.bool] = None,
        allow_squash_merge: typing.Optional[builtins.bool] = None,
        archived: typing.Optional[builtins.bool] = None,
        archive_on_destroy: typing.Optional[builtins.bool] = None,
        auto_init: typing.Optional[builtins.bool] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[builtins.bool] = None,
        has_issues: typing.Optional[builtins.bool] = None,
        has_projects: typing.Optional[builtins.bool] = None,
        has_wiki: typing.Optional[builtins.bool] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[builtins.bool] = None,
        license_template: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Sequence["PagesDefinition"]] = None,
        private: typing.Optional[builtins.bool] = None,
        template: typing.Optional[typing.Sequence["TemplateDefinition"]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This resource allows you to create and manage repositories within your GitHub organization or personal account.

        :param name: The name of the repository.
        :param allow_merge_commit: Set to ``false`` to disable merge commits on the repository.
        :param allow_rebase_merge: Set to ``false`` to disable rebase merges on the repository.
        :param allow_squash_merge: Set to ``false`` to disable squash merges on the repository.
        :param archived: Specifies if the repository should be archived. Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving. Default: false`. **NOTE** Currently, the API does not support unarchiving.
        :param archive_on_destroy: Set to ``true`` to archive the repository instead of deleting on destroy.
        :param auto_init: Set to ``true`` to produce an initial commit in the repository.
        :param default_branch: (Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created, and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the initial repository creation and create the target branch inside of the repository prior to setting this attribute.
        :param delete_branch_on_merge: Automatically delete head branch after a pull request is merged. Defaults to ``false``. Default: false`.
        :param description: A description of the repository.
        :param gitignore_template: Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".
        :param has_downloads: Set to ``true`` to enable the (deprecated) downloads features on the repository.
        :param has_issues: Set to ``true`` to enable the GitHub Issues features on the repository.
        :param has_projects: Set to ``true`` to enable the GitHub Projects features on the repository. Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.
        :param has_wiki: Set to ``true`` to enable the GitHub Wiki features on the repository.
        :param homepage_url: URL of a page describing the project.
        :param is_template: Set to ``true`` to tell GitHub that this is a template repository.
        :param license_template: Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".
        :param pages: 
        :param private: Set to ``true`` to create a private repository. Repositories are created as public (e.g. open source) by default.
        :param template: 
        :param topics: The list of topics of the repository.
        :param visibility: Can be ``public`` or ``private``. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.
        :param vulnerability_alerts: 

        :schema: CfnRepositoryProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allow_merge_commit is not None:
            self._values["allow_merge_commit"] = allow_merge_commit
        if allow_rebase_merge is not None:
            self._values["allow_rebase_merge"] = allow_rebase_merge
        if allow_squash_merge is not None:
            self._values["allow_squash_merge"] = allow_squash_merge
        if archived is not None:
            self._values["archived"] = archived
        if archive_on_destroy is not None:
            self._values["archive_on_destroy"] = archive_on_destroy
        if auto_init is not None:
            self._values["auto_init"] = auto_init
        if default_branch is not None:
            self._values["default_branch"] = default_branch
        if delete_branch_on_merge is not None:
            self._values["delete_branch_on_merge"] = delete_branch_on_merge
        if description is not None:
            self._values["description"] = description
        if gitignore_template is not None:
            self._values["gitignore_template"] = gitignore_template
        if has_downloads is not None:
            self._values["has_downloads"] = has_downloads
        if has_issues is not None:
            self._values["has_issues"] = has_issues
        if has_projects is not None:
            self._values["has_projects"] = has_projects
        if has_wiki is not None:
            self._values["has_wiki"] = has_wiki
        if homepage_url is not None:
            self._values["homepage_url"] = homepage_url
        if is_template is not None:
            self._values["is_template"] = is_template
        if license_template is not None:
            self._values["license_template"] = license_template
        if pages is not None:
            self._values["pages"] = pages
        if private is not None:
            self._values["private"] = private
        if template is not None:
            self._values["template"] = template
        if topics is not None:
            self._values["topics"] = topics
        if visibility is not None:
            self._values["visibility"] = visibility
        if vulnerability_alerts is not None:
            self._values["vulnerability_alerts"] = vulnerability_alerts

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the repository.

        :schema: CfnRepositoryProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_merge_commit(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable merge commits on the repository.

        :schema: CfnRepositoryProps#AllowMergeCommit
        '''
        result = self._values.get("allow_merge_commit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_rebase_merge(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable rebase merges on the repository.

        :schema: CfnRepositoryProps#AllowRebaseMerge
        '''
        result = self._values.get("allow_rebase_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_squash_merge(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable squash merges on the repository.

        :schema: CfnRepositoryProps#AllowSquashMerge
        '''
        result = self._values.get("allow_squash_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def archived(self) -> typing.Optional[builtins.bool]:
        '''Specifies if the repository should be archived.

        Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving.

        :default: false`. **NOTE** Currently, the API does not support unarchiving.

        :schema: CfnRepositoryProps#Archived
        '''
        result = self._values.get("archived")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def archive_on_destroy(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to archive the repository instead of deleting on destroy.

        :schema: CfnRepositoryProps#ArchiveOnDestroy
        '''
        result = self._values.get("archive_on_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_init(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to produce an initial commit in the repository.

        :schema: CfnRepositoryProps#AutoInit
        '''
        result = self._values.get("auto_init")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_branch(self) -> typing.Optional[builtins.str]:
        '''(Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository.

        **NOTE:** This can only be set after a repository has already been created,
        and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
        initial repository creation and create the target branch inside of the repository prior to setting this attribute.

        :schema: CfnRepositoryProps#DefaultBranch
        '''
        result = self._values.get("default_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_branch_on_merge(self) -> typing.Optional[builtins.bool]:
        '''Automatically delete head branch after a pull request is merged.

        Defaults to ``false``.

        :default: false`.

        :schema: CfnRepositoryProps#DeleteBranchOnMerge
        '''
        result = self._values.get("delete_branch_on_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the repository.

        :schema: CfnRepositoryProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gitignore_template(self) -> typing.Optional[builtins.str]:
        '''Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".

        :schema: CfnRepositoryProps#GitignoreTemplate
        '''
        result = self._values.get("gitignore_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def has_downloads(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the (deprecated) downloads features on the repository.

        :schema: CfnRepositoryProps#HasDownloads
        '''
        result = self._values.get("has_downloads")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_issues(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Issues features on the repository.

        :schema: CfnRepositoryProps#HasIssues
        '''
        result = self._values.get("has_issues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_projects(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Projects features on the repository.

        Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.

        :schema: CfnRepositoryProps#HasProjects
        '''
        result = self._values.get("has_projects")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_wiki(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Wiki features on the repository.

        :schema: CfnRepositoryProps#HasWiki
        '''
        result = self._values.get("has_wiki")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def homepage_url(self) -> typing.Optional[builtins.str]:
        '''URL of a page describing the project.

        :schema: CfnRepositoryProps#HomepageUrl
        '''
        result = self._values.get("homepage_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_template(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to tell GitHub that this is a template repository.

        :schema: CfnRepositoryProps#IsTemplate
        '''
        result = self._values.get("is_template")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def license_template(self) -> typing.Optional[builtins.str]:
        '''Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".

        :schema: CfnRepositoryProps#LicenseTemplate
        '''
        result = self._values.get("license_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pages(self) -> typing.Optional[typing.List["PagesDefinition"]]:
        '''
        :schema: CfnRepositoryProps#Pages
        '''
        result = self._values.get("pages")
        return typing.cast(typing.Optional[typing.List["PagesDefinition"]], result)

    @builtins.property
    def private(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to create a private repository.

        Repositories are created as public (e.g. open source) by default.

        :schema: CfnRepositoryProps#Private
        '''
        result = self._values.get("private")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def template(self) -> typing.Optional[typing.List["TemplateDefinition"]]:
        '''
        :schema: CfnRepositoryProps#Template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.List["TemplateDefinition"]], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of topics of the repository.

        :schema: CfnRepositoryProps#Topics
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Can be ``public`` or ``private``.

        If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.

        :schema: CfnRepositoryProps#Visibility
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vulnerability_alerts(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnRepositoryProps#VulnerabilityAlerts
        '''
        result = self._values.get("vulnerability_alerts")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.PagesDefinition",
    jsii_struct_bases=[],
    name_mapping={"cname": "cname", "source": "source"},
)
class PagesDefinition:
    def __init__(
        self,
        *,
        cname: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Sequence["SourceDefinition"]] = None,
    ) -> None:
        '''
        :param cname: 
        :param source: 

        :schema: PagesDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cname is not None:
            self._values["cname"] = cname
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def cname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: PagesDefinition#Cname
        '''
        result = self._values.get("cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[typing.List["SourceDefinition"]]:
        '''
        :schema: PagesDefinition#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.List["SourceDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.SourceDefinition",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "path": "path"},
)
class SourceDefinition:
    def __init__(
        self,
        *,
        branch: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: 
        :param path: 

        :schema: SourceDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def branch(self) -> builtins.str:
        '''
        :schema: SourceDefinition#Branch
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SourceDefinition#Path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.TemplateDefinition",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner", "repository": "repository"},
)
class TemplateDefinition:
    def __init__(self, *, owner: builtins.str, repository: builtins.str) -> None:
        '''
        :param owner: 
        :param repository: 

        :schema: TemplateDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "owner": owner,
            "repository": repository,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''
        :schema: TemplateDefinition#Owner
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''
        :schema: TemplateDefinition#Repository
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRepository",
    "CfnRepositoryProps",
    "PagesDefinition",
    "SourceDefinition",
    "TemplateDefinition",
]

publication.publish()
