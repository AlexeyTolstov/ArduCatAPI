from faker import Faker
from random import randint, choice

fake = Faker("RU_ru")

def random_bool() -> bool:
    return choice([True, False])


class ExampleUserData:
    """Example user data for testing."""

    """Correct user data"""
    correct_user_data = [
        {
            "login": "bojankorolev",
            "password": "cXODffzpkTTSynVX",
            "first_name": "Михаил",
            "last_name": "Абрамова",
            "email": "natalja04@example.com"
        },
        {
            "login": "efim2009",
            "password": "J+mvI#yL@9R@0ZlRbVLh",
            "first_name": "Федор",
            "last_name": "Тетерин",
            "email": "kotovdobroslav@example.net"
        },
        {
            "login": "fbirjukov",
            "password": "a2o3qwHOrQMC3Kkib",
            "first_name": "Измаил",
            "last_name": "Семенова",
            "email": "blinovaregina@example.org"
        }
    ]

    """INCORRECT USER DATA"""

    """No fields in user data"""
    no_field_user_data = [
        {},
        {"first_name": "Федот", "last_name": "Герасимов"},
        {"login": "sisoevamarfa", "password": "rHSTrrXKnq"},
        {"login": "viktorin1988", "email": "elizar2007@example.com"},
        {"password": "wZZ9mZ9x", "first_name": "Татьяна", "last_name": "Егорова", "email": "nikolaevalukija@example.org"}
    ]

    """Incorrect fields"""
    incorrects_field_user_data = [
        # Incorrect login
        {
            "login": "HI",
            "password": "cXODffzpkTTSynVX",
            "first_name": "Михаил",
            "last_name": "Абрамова",
            "email": "natalja04@example.com"
        },

        # Incorrect password
        {
            "login": "efim2009",
            "password": "ZlRVLh",
            "first_name": "Федор",
            "last_name": "Тетерин",
            "email": "kotovdobroslav@example.net"
        },

        # Incorrect email 
        {
            "login": "fbirjukov",
            "password": "a2o3qwHOrQMC3Kkib",
            "first_name": "Измаил",
            "last_name": "Семенова",
            "email": "bububu.org"
        }
    ]


def generate_correct_user_data() -> dict:
    login: str = fake.user_name()

    password: str = fake.password(
        length=randint(8, 20),
        special_chars=random_bool(),
        digits=random_bool(),
    )

    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    email: str = fake.email()

    return {
        "login": login,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }