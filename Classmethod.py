class Subject:
    """A class to represent a Subject."""

    # Class variable
    favorite_subject = "Python"

    @classmethod
    def get_favorite_subject(cls):
        """
        Class method to print the favorite subject stored in the class variable.
        """
        print("My favorite subject is:", cls.favorite_subject)


def main():
    """
    Main function to execute script tasks.
    """
    # Calling the class method using the class name
    Subject.get_favorite_subject()


if __name__ == "__main__":
    main()
