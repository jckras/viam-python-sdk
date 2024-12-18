"""
@generated by Viam.
Do not edit manually!
"""

from ...gen.app.v1.app_grpc import AppServiceBase, AppServiceStub, UnimplementedAppServiceBase
from ...gen.app.v1.app_pb2 import (
    AddRoleRequest,
    AddRoleResponse,
    APIKey,
    APIKeyWithAuthorizations,
    AuthenticationType,
    AuthenticatorInfo,
    Authorization,
    AuthorizationDetails,
    AuthorizedPermissions,
    BillingAddress,
    ChangeRoleRequest,
    ChangeRoleResponse,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    CreateKeyFromExistingKeyAuthorizationsRequest,
    CreateKeyFromExistingKeyAuthorizationsResponse,
    CreateKeyRequest,
    CreateKeyResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateRegistryItemRequest,
    CreateRegistryItemResponse,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteFragmentResponse,
    DeleteKeyRequest,
    DeleteKeyResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteLocationSecretRequest,
    DeleteLocationSecretResponse,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationInviteResponse,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationMemberResponse,
    DeleteOrganizationRequest,
    DeleteOrganizationResponse,
    DeleteRegistryItemRequest,
    DeleteRegistryItemResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    DeleteRobotPartSecretRequest,
    DeleteRobotPartSecretResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    DisableBillingServiceRequest,
    DisableBillingServiceResponse,
    EnableBillingServiceRequest,
    EnableBillingServiceResponse,
    Fragment,
    FragmentError,
    FragmentErrorType,
    FragmentHistoryEntry,
    FragmentTree,
    FragmentVisibility,
    GetFragmentHistoryRequest,
    GetFragmentHistoryResponse,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    GetOrganizationRequest,
    GetOrganizationResponse,
    GetOrganizationsWithAccessToLocationRequest,
    GetOrganizationsWithAccessToLocationResponse,
    GetRegistryItemRequest,
    GetRegistryItemResponse,
    GetRobotAPIKeysRequest,
    GetRobotAPIKeysResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListKeysRequest,
    ListKeysResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListMachineFragmentsRequest,
    ListMachineFragmentsResponse,
    ListModulesRequest,
    ListModulesResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    ListOrganizationsByUserRequest,
    ListOrganizationsByUserResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRegistryItemsRequest,
    ListRegistryItemsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
    LocationOrganization,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    MLModelMetadata,
    MLTrainingMetadata,
    MLTrainingVersion,
    Model,
    Module,
    ModuleFileInfo,
    ModuleMetadata,
    ModuleVersion,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    OrganizationGetSupportEmailRequest,
    OrganizationGetSupportEmailResponse,
    OrganizationIdentity,
    OrganizationInvite,
    OrganizationMember,
    OrganizationSetSupportEmailRequest,
    OrganizationSetSupportEmailResponse,
    OrgDetails,
    RegistryItem,
    RegistryItemStatus,
    RemoveRoleRequest,
    RemoveRoleResponse,
    RenameKeyRequest,
    RenameKeyResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
    RobotPart,
    RobotPartHistoryEntry,
    RotateKeyRequest,
    RotateKeyResponse,
    RoverRentalRobot,
    SharedSecret,
    ShareLocationRequest,
    ShareLocationResponse,
    StorageConfig,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    TransferRegistryItemRequest,
    TransferRegistryItemResponse,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateBillingServiceRequest,
    UpdateBillingServiceResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRegistryItemResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
    Uploads,
    VersionHistory,
    Visibility,
)

__all__ = [
    "AppServiceBase",
    "AppServiceStub",
    "UnimplementedAppServiceBase",
    "APIKey",
    "APIKeyWithAuthorizations",
    "AddRoleRequest",
    "AddRoleResponse",
    "AuthenticationType",
    "AuthenticatorInfo",
    "Authorization",
    "AuthorizationDetails",
    "AuthorizedPermissions",
    "BillingAddress",
    "ChangeRoleRequest",
    "ChangeRoleResponse",
    "CheckPermissionsRequest",
    "CheckPermissionsResponse",
    "CreateFragmentRequest",
    "CreateFragmentResponse",
    "CreateKeyFromExistingKeyAuthorizationsRequest",
    "CreateKeyFromExistingKeyAuthorizationsResponse",
    "CreateKeyRequest",
    "CreateKeyResponse",
    "CreateLocationRequest",
    "CreateLocationResponse",
    "CreateLocationSecretRequest",
    "CreateLocationSecretResponse",
    "CreateModuleRequest",
    "CreateModuleResponse",
    "CreateOrganizationInviteRequest",
    "CreateOrganizationInviteResponse",
    "CreateOrganizationRequest",
    "CreateOrganizationResponse",
    "CreateRegistryItemRequest",
    "CreateRegistryItemResponse",
    "CreateRobotPartSecretRequest",
    "CreateRobotPartSecretResponse",
    "DeleteFragmentRequest",
    "DeleteFragmentResponse",
    "DeleteKeyRequest",
    "DeleteKeyResponse",
    "DeleteLocationRequest",
    "DeleteLocationResponse",
    "DeleteLocationSecretRequest",
    "DeleteLocationSecretResponse",
    "DeleteOrganizationInviteRequest",
    "DeleteOrganizationInviteResponse",
    "DeleteOrganizationMemberRequest",
    "DeleteOrganizationMemberResponse",
    "DeleteOrganizationRequest",
    "DeleteOrganizationResponse",
    "DeleteRegistryItemRequest",
    "DeleteRegistryItemResponse",
    "DeleteRobotPartRequest",
    "DeleteRobotPartResponse",
    "DeleteRobotPartSecretRequest",
    "DeleteRobotPartSecretResponse",
    "DeleteRobotRequest",
    "DeleteRobotResponse",
    "DisableBillingServiceRequest",
    "DisableBillingServiceResponse",
    "EnableBillingServiceRequest",
    "EnableBillingServiceResponse",
    "Fragment",
    "FragmentError",
    "FragmentErrorType",
    "FragmentHistoryEntry",
    "FragmentTree",
    "FragmentVisibility",
    "GetFragmentHistoryRequest",
    "GetFragmentHistoryResponse",
    "GetFragmentRequest",
    "GetFragmentResponse",
    "GetLocationRequest",
    "GetLocationResponse",
    "GetModuleRequest",
    "GetModuleResponse",
    "GetOrganizationNamespaceAvailabilityRequest",
    "GetOrganizationNamespaceAvailabilityResponse",
    "GetOrganizationRequest",
    "GetOrganizationResponse",
    "GetOrganizationsWithAccessToLocationRequest",
    "GetOrganizationsWithAccessToLocationResponse",
    "GetRegistryItemRequest",
    "GetRegistryItemResponse",
    "GetRobotAPIKeysRequest",
    "GetRobotAPIKeysResponse",
    "GetRobotPartHistoryRequest",
    "GetRobotPartHistoryResponse",
    "GetRobotPartLogsRequest",
    "GetRobotPartLogsResponse",
    "GetRobotPartRequest",
    "GetRobotPartResponse",
    "GetRobotPartsRequest",
    "GetRobotPartsResponse",
    "GetRobotRequest",
    "GetRobotResponse",
    "GetRoverRentalRobotsRequest",
    "GetRoverRentalRobotsResponse",
    "GetUserIDByEmailRequest",
    "GetUserIDByEmailResponse",
    "ListAuthorizationsRequest",
    "ListAuthorizationsResponse",
    "ListFragmentsRequest",
    "ListFragmentsResponse",
    "ListKeysRequest",
    "ListKeysResponse",
    "ListLocationsRequest",
    "ListLocationsResponse",
    "ListMachineFragmentsRequest",
    "ListMachineFragmentsResponse",
    "ListModulesRequest",
    "ListModulesResponse",
    "ListOrganizationMembersRequest",
    "ListOrganizationMembersResponse",
    "ListOrganizationsByUserRequest",
    "ListOrganizationsByUserResponse",
    "ListOrganizationsRequest",
    "ListOrganizationsResponse",
    "ListRegistryItemsRequest",
    "ListRegistryItemsResponse",
    "ListRobotsRequest",
    "ListRobotsResponse",
    "Location",
    "LocationAuth",
    "LocationAuthRequest",
    "LocationAuthResponse",
    "LocationOrganization",
    "MLModelMetadata",
    "MLTrainingMetadata",
    "MLTrainingVersion",
    "MarkPartAsMainRequest",
    "MarkPartAsMainResponse",
    "MarkPartForRestartRequest",
    "MarkPartForRestartResponse",
    "Model",
    "Module",
    "ModuleFileInfo",
    "ModuleMetadata",
    "ModuleVersion",
    "NewRobotPartRequest",
    "NewRobotPartResponse",
    "NewRobotRequest",
    "NewRobotResponse",
    "OrgDetails",
    "Organization",
    "OrganizationGetSupportEmailRequest",
    "OrganizationGetSupportEmailResponse",
    "OrganizationIdentity",
    "OrganizationInvite",
    "OrganizationMember",
    "OrganizationSetSupportEmailRequest",
    "OrganizationSetSupportEmailResponse",
    "RegistryItem",
    "RegistryItemStatus",
    "RemoveRoleRequest",
    "RemoveRoleResponse",
    "RenameKeyRequest",
    "RenameKeyResponse",
    "ResendOrganizationInviteRequest",
    "ResendOrganizationInviteResponse",
    "Robot",
    "RobotPart",
    "RobotPartHistoryEntry",
    "RotateKeyRequest",
    "RotateKeyResponse",
    "RoverRentalRobot",
    "ShareLocationRequest",
    "ShareLocationResponse",
    "SharedSecret",
    "StorageConfig",
    "TailRobotPartLogsRequest",
    "TailRobotPartLogsResponse",
    "TransferRegistryItemRequest",
    "TransferRegistryItemResponse",
    "UnshareLocationRequest",
    "UnshareLocationResponse",
    "UpdateBillingServiceRequest",
    "UpdateBillingServiceResponse",
    "UpdateFragmentRequest",
    "UpdateFragmentResponse",
    "UpdateLocationRequest",
    "UpdateLocationResponse",
    "UpdateModuleRequest",
    "UpdateModuleResponse",
    "UpdateOrganizationInviteAuthorizationsRequest",
    "UpdateOrganizationInviteAuthorizationsResponse",
    "UpdateOrganizationRequest",
    "UpdateOrganizationResponse",
    "UpdateRegistryItemRequest",
    "UpdateRegistryItemResponse",
    "UpdateRobotPartRequest",
    "UpdateRobotPartResponse",
    "UpdateRobotRequest",
    "UpdateRobotResponse",
    "UploadModuleFileRequest",
    "UploadModuleFileResponse",
    "Uploads",
    "VersionHistory",
    "Visibility",
]
