from app.models import Users, JobPost
from passlib.hash import bcrypt_sha256


# used for name and email checks in a registration process
def checkExistence(name, email):
    exist_name = Users.query.filter_by(name=name).first()
    exist_email = Users.query.filter_by(email=email).first()
    errors = []
    if exist_name:
        errors.append("Your user name has been used. Pls use a new name.")
    if exist_email:
        errors.append("Your email has been registered. Pls try a new one.")
    return errors


# used for name and password checks when trying to login in with username
def checkByName(name, password):
    user = Users.query.filter_by(name=name).first()
    errors = []
    if user is None:
        errors.append("No such user exists, pls check your inputs.")
    elif not bcrypt_sha256.verify(str(password), user.password):
        errors.append("Password does not match the given user. Pls try again.")
    return errors


# used for email and password checks when trying to login in with email
def checkByEmail(email, password):
    user = Users.query.filter_by(email=email).first()
    errors = []
    if user is None:
        errors.append("No user with this email exists, pls check your inputs.")
    elif not bcrypt_sha256.verify(str(password), user.password):
        errors.append("Password does not match the given user. Pls try again.")
    return errors


def create_post(record):
    post = {}
    post["post_id"] = record.post_id
    post["title"] = record.title
    post["link"] = "https://" + record.link
    post["company"] = record.company
    post["salary_min"] = record.salary_min
    post["salary_max"] = record.salary_max
    post["salary"] = "not given" if record.salary_max == 0 else " - ".join(["$" + str(record.salary_min), "$" + str(record.salary_max)])
    post["date"] = record.date

    return post