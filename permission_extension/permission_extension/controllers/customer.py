# import frappe
# from permission_extension.permission_extension.utils import get_permission_settings


# def get_permission_query_conditions(user):
#     permission_settings = get_permission_settings()
#     if not permission_settings.get("customer_permission"):
#         return ""
    
#     if not user:
#         user = frappe.session.user
#     if user == "Administrator":
#         return ""

#     allowed_companies = get_allowed_values(user, "Company")
#     if not allowed_companies:
#         return ""
    
#     if allowed_companies:
#         allowed_companies_str = ", ".join([f"'{b}'" for b in allowed_companies])
        
#         return f"""
#              EXISTS (
#                     SELECT 1 FROM `tabParty Account` AS d2
#                     WHERE d2.parent = `tabCustomer`.name
#                     AND d2.company IN ({allowed_companies_str})
                
#             )
#         """
    
# def get_allowed_values(user, doctype):
#     return frappe.get_all(
#         "User Permission",
#         filters={"user": user, "allow": doctype},
#         pluck="for_value"
#     )
