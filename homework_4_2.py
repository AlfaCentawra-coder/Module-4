def test_function():
    def inner_function():
        print("Я нахожусь в зоне видимости test_function")
    inner_function()

test_function()

inner_function() # глобальное пространство не видит функцию inner_function, так как она находится в локальном пространстве test_function (NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?)