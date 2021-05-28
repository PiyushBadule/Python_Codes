class Subject:
    # create a variable
    favorite_subject = "Python"

    # create a function
    def favorite_subject_name(obj):
        print("My favorite subject name is : ",
              obj.favorite_subject)

    # create favorite_subject_name classmethod


# before creating this line favorite_subject_name()
# It can be called only with object not with class
Subject.name = classmethod(Subject.favorite_subject_name)

# now this method can be called as classmethod
# favorite_subject_name() method is called as class method
Subject.name()