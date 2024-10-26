from exc import PhoneVerificationError, EmailVerificationError, OwnerError, NoUserError, NoteExistError


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TypeError:
            return "The command don't need args"
        except IndexError:
            return "The command need more args"
        except KeyError:
            return "The command is unknown"
        except PhoneVerificationError:
            return "The phone number incorrect 3 + 7 phone digits. Try again!"
        except EmailVerificationError:
            return "Email is not valid. Try again!"
        except OwnerError:
            return "The phone number is related with other contact"
        except NoUserError:
            return "AddressBook hasn't the contact name yet, please add before change"
        except ValueError:
            return "Something goes wrong. Input 'help' for manual"
        except FileNotFoundError:
            return "Entered folder does not exists. Please provide correct path to folder"
        except NoteExistError:
            return "This note already exists"

    return inner
