from project import encrypt_password, decrypt_password, add_new_password


def test_encrypt_password():
    assert encrypt_password(1, "abc") == "bcd"
    assert encrypt_password(1, "xyz") == "yzA"
    assert encrypt_password(1, "123") == "234"
    assert encrypt_password(1, "abc123") == "bcd234"
    
    

def test_decrypt_password():
    assert decrypt_password("bcd", 1) == "abc"
    assert decrypt_password("yzA", 1) == "xyz"
    assert decrypt_password("234", 1) == "123"
    assert decrypt_password("bcd234", 1) == "abc123"


def test_add_new_password():
    assert add_new_password("facebook.com", "username", "password") == ['password','facebook.com','username\n']
    assert add_new_password("gmail.com", "username", "password") == ['password','gmail.com','username\n']
    assert add_new_password("twitter.com", "username", "password") == ['password','twitter.com','username\n']