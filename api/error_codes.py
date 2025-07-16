# Error Codes for API Responses

AUTH_ERROR_CODES = {
    'AS1001': 'InvalidRegistrationData',
    'AS1002': 'EmailAlreadyExists',
    'AS1003': 'InvalidLoginCredentials',
    'AS1004': 'UserNotFound',
    'AS1005': 'AuthenticationRequired',
    'AS1006': 'InvalidLogoutToken',
}

PROJECT_ERROR_CODES = {
    'AS2001': 'ProjectNotFound',
    'AS2002': 'InvalidProjectData',
    'AS2003': 'ProjectCreationFailed',
    'AS2004': 'ProjectUpdateFailed',
    'AS2005': 'ProjectDeleteFailed',
}

EMPLOYEE_ERROR_CODES = {
    'AS3001': 'EmployeeNotFound',
    'AS3002': 'InvalidEmployeeData',
    'AS3003': 'EmployeeCreationFailed',
    'AS3004': 'EmployeeUpdateFailed',
    'AS3005': 'EmployeeDeleteFailed',
}

INVESTOR_ERROR_CODES = {
    'AS4001': 'InvestorProfileNotFound',
    'AS4002': 'InvalidInvestorData',
    'AS4003': 'InvestorProfileCreationFailed',
    'AS4004': 'InvestorProfileUpdateFailed',
    'AS4005': 'InvestorProfileDeleteFailed',
}

DOCUMENT_ERROR_CODES = {
    'AS5001': 'LegalDocumentNotFound',
    'AS5002': 'InvalidDocumentData',
    'AS5003': 'DocumentCreationFailed',
    'AS5004': 'DocumentUpdateFailed',
    'AS5005': 'DocumentDeleteFailed',
}

FILE_ERROR_CODES = {
    'AS6001': 'FileUploadFailed',
    'AS6002': 'InvalidFileType',
    'AS6003': 'FileTooLarge',
}

# Combine all error codes
ALL_ERROR_CODES = {
    **AUTH_ERROR_CODES,
    **PROJECT_ERROR_CODES,
    **EMPLOYEE_ERROR_CODES,
    **INVESTOR_ERROR_CODES,
    **DOCUMENT_ERROR_CODES,
    **FILE_ERROR_CODES,
} 