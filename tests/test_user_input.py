from user_input import confirm,get_valid_password,get_valid_username
import builtins
import pytest
import policies
import storage
# below import needed to properly mock check_username_exitence
import user_input.user_input as ui

class Fake_Sequencial_Inputs:
    def __init__(self,inputs):
        self.inputs = list(inputs)
        self.index = 0
    
    def __call__(self,prompt):
        if self.index >= len(self.inputs):
            raise IndexError("No more fake inputs provided")
        input = self.inputs[self.index]
        self.index += 1
        return input

@pytest.fixture
def fake_input_sequence():
# fake sequencial inputs factory
    def fake_input_factory(inputs):
        return Fake_Sequencial_Inputs(inputs)
    return fake_input_factory
        
@pytest.fixture
def valid_username():
    return "lucas"

@pytest.fixture
def invalid_username():
    return "thisusernameiswaytoobig!!!!!!"

@pytest.fixture
def valid_password():
    return "V@lidPassw0rd"

@pytest.fixture
def invalid_password():
    return "invalid"



def test_confirm_invalid_user_answer_and_exit(monkeypatch,capsys,fake_input_sequence):
# last value is "" for it to call sys exit as it does in the confirm function. 
    invalid_sequence = fake_input_sequence(["j","lol","fake","whatever",""])
    monkeypatch.setattr(builtins,"input",invalid_sequence)
    with pytest.raises(SystemExit):
        confirm("Example question")

    output = capsys.readouterr().out
# 4 invalid outputs provided for the loop
    assert output.count("Invalid answer.") == 4

@pytest.mark.parametrize(
    ("user_input","expected"),
[
    ("Y", True),
    ("y", True),
    ("N", False),
    ("n", False),
    ("    n    ", False),
    ("     Y     ", True)
]
)

def test_confirm_valid_user_is_case_insensitive(monkeypatch,user_input,expected):
    monkeypatch.setattr(builtins,"input",lambda _: user_input)
    answer = confirm("Example question")
    assert answer is expected

def test_confirm_message_passed_to_input(monkeypatch):
    captured = []

    def fake_input(prompt):
        captured.append(prompt)
        return "" # user presses enter to exit
    
    monkeypatch.setattr(builtins,"input",fake_input)

    try:
        confirm("Example question")
    except SystemExit:
        pass # user pressed enter
    
    assert captured,"input was not called" # if input is not in "captured", "input was not called" will be displayed by pytest AssertionError
    assert "Example question" in captured[0] #captured is a list, to use "in" we must use the index, even though there's no other elements in the list


def test_get_valid_username_loop_interaction_invalid_then_valid(monkeypatch,capsys,fake_input_sequence,valid_username,invalid_username):
    def mock_check_username_existence(username_input):
        return False
    def mock_username_policy(username_input):
        return username_input == valid_username
    monkeypatch.setattr(ui.storage,"check_username_existence",mock_check_username_existence)
    monkeypatch.setattr(ui.policies,"username_policy",mock_username_policy)

# tests interaction > input invalid username > asks for another username > inputs valid username

# > answers "N" > asks for another username > inputs valid username > input "Y" to confirm username
    fake_inputs = fake_input_sequence([invalid_username,valid_username,"N",valid_username,"Y"])
    monkeypatch.setattr(builtins,"input",fake_inputs)
    chosen_username = get_valid_username()
    output = capsys.readouterr().out
    assert f"{invalid_username} is not a valid username." in output, "invalid username warning didn't show up for the user"
    assert chosen_username == valid_username, "returned username didn't match"

def test_get_valid_password_loop_interaction_invalid_then_valid(monkeypatch,capsys,fake_input_sequence,valid_password,invalid_password):
    def mock_password_policy(password_input):
        return password_input == valid_password
    def mock_security_feedback(invalid_password_input):
        print(f"Security feedback was called")
    monkeypatch.setattr(ui.policies,"password_policy",mock_password_policy)
    monkeypatch.setattr(ui.policies,"security_feedback",mock_security_feedback)
# tests interaction > input invalid password > asks for another password > input valid password 
# > input invalid password in the double check confirmation of the password > states the password don't match > starts all over > asks for password
# > inputs valid password, inputs valid password and passes the double check > finish
    fake_inputs = fake_input_sequence([invalid_password,valid_password,invalid_password,valid_password,valid_password])
    monkeypatch.setattr(builtins,"input",fake_inputs)
    chosen_password = get_valid_password()
    output = capsys.readouterr().out
    assert "Didn't match." in output
    assert chosen_password == valid_password


