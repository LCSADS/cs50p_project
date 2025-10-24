import re
import pytest
import policies
import builtins
        

@pytest.mark.parametrize(
    ("password_input","expected_output"),
    [
        ("V@l1ddPassword",True), # valid
        ("invalidpassword",False), # missing number, special character and capital letter
        ("Sh0rt!",False), # under 8 characters
        ("Th!spassw0rdiswaytoobig",False), # over 16 characters
        ("NoNumber!",False), # missing number
        ("l0w3rc@se",False), # missing upper case
        ("@LLCAPS1!!1!",False), # missing lower case 
        ("n0speclCharacter",False), # no special character
        ("",False), #empty
    ],
    ids=[
        "valid","missing_several_requirements","short","big","no_number","no_upper_case","no_lower_case","no_special_characters","empty"
    ],
)


def test_password_policy(password_input,expected_output):
    output = policies.password_policy(password_input)
    assert output is expected_output


@pytest.mark.parametrize(
    ("password_input","expected_output"),
    [(
        "",{"Lenght between 8 and 16 characters.",
          "At least one number",
          "At least one special character",
          "At least one lower letter.",
          "At least one capital letter.",
          }
    ),
    ("Th!spassw0rdiswaytoobig","Lenght between 8 and 16 characters."),
    ("l0w3rc@se","At least one capital letter."),
    ("@LLCAPS1!!1!","At least one lower letter."),
    ("n0speclCharacter","At least one special character"),
    ("NoNumber!","At least one number"),
    

    ]


)

def test_security_feedback(password_input,expected_output,monkeypatch,capsys):
    monkeypatch.setattr(builtins,"input",lambda _: password_input)
    policies.security_feedback(password_input)
    output = capsys.readouterr().out
    for string in expected_output:
        assert string in output



# expected feedback messages for invalid username

lenght_msg = "In between 5 and 20 characters."
startswith_msg = "The starting character must be a letter"
endswithmsg = "The last character should be a letter or a number."
invalid_characters_msg = "Only letters, digits, dots, underscores and hyphens are allowed"
separators_repetition_msg = "No two separators in a row. I.E : ._ or .. or __"
characters_repetition_msg = "No characters can appear 3 times in a row."

@pytest.mark.parametrize(
        ("username_input","expected_feedback"),
        [
           # invalid lenght 
            
            ("abc1",{lenght_msg}), # under 5 characters
            ("thisusernameiswaytoobig!!!!!",{lenght_msg}), # over 20 characters
            
           # invalid start
            
            ("1lucas",{startswith_msg}), # starts with a number
            (".lucas",{startswith_msg}), # starts with a dot
            ("_lucas",{startswith_msg}), # starts with a underscore
            ("-lucas",{startswith_msg}), # starts with a hyphen
            
            # invalid ending
            
            ("lucas.",{endswithmsg}),
            ("lucas_",{endswithmsg}),
            ("lucas-",{endswithmsg}),
            
            # invalid characters

            ("lucas user",{invalid_characters_msg}), # blank space
            ("luc@s",{invalid_characters_msg}), # @
            ("lúcas",{invalid_characters_msg}), # non ASCII
          

          # two separators in a row

            ("lu__cas",{separators_repetition_msg}),  
            ("lu..cas",{separators_repetition_msg}),  
            ("lu--cas",{separators_repetition_msg}),  
            ("lu_.cas",{separators_repetition_msg}),  
            ("lu-.cas",{separators_repetition_msg}), 

          # 3 character repetition
            ("luuucas",{characters_repetition_msg}),  
            ("LLLucas",{characters_repetition_msg}),  
            ("lucas777",{characters_repetition_msg}),  

        ],
)




def test_invalid_username_feedback_messages(username_input,capsys,expected_feedback):
    policies.invalid_username_feedback(username_input)
    output = capsys.readouterr().out
    for message in expected_feedback:
        assert message in output


def test_invalid_username_gives_no_feedback_to_valid_usernames(capsys):
    valid_username = "lucas123"
    policies.invalid_username_feedback(valid_username)
    output = capsys.readouterr().out
    assert len(output) == 0