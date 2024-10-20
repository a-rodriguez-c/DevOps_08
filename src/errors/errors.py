

class ApiError(Exception):
    code = 422
    description = "Default message"  

class InvalidParams(ApiError):
    code = 400
    description = "Invalid parameters."

class EmailAlreadyBlacklisted(ApiError):
    code = 409
    description = "The email is already blacklisted."
    
class EmailNotFound(ApiError):
    code = 404
    description = "Email not found."