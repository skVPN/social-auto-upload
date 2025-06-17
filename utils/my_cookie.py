from setting import COOKIE_DB
def get_all_cookie():
    rows = COOKIE_DB.find("SELECT \
    pk AS id,\
    CASE \
        WHEN domain = 'tiktok.com' THEN 5 \
        ELSE 0 \
    END AS type,\
    b_id AS file_path,\
    account_name AS userName,\
    is_effect AS status  \
FROM feapder.cookie_api""")
    
    return  rows
