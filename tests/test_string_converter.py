import pytest
from src.string_converter import to_kebab_case

def test_to_kebab_case_camel_case():
    assert to_kebab_case("helloWorld") == "hello-world"
    assert to_kebab_case("convertToKebabCase") == "convert-to-kebab-case"

def test_to_kebab_case_pascal_case():
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("ConvertToKebabCase") == "convert-to-kebab-case"

def test_to_kebab_case_snake_case():
    assert to_kebab_case("hello_world") == "hello-world"
    assert to_kebab_case("convert_to_kebab_case") == "convert-to-kebab-case"

def test_to_kebab_case_space_separated():
    assert to_kebab_case("hello world") == "hello-world"
    assert to_kebab_case("Convert To Kebab Case") == "convert-to-kebab-case"

def test_to_kebab_case_mixed_separators():
    assert to_kebab_case("hello_World Test Case") == "hello-world-test-case"
    assert to_kebab_case("convert__to-Kebab_Case") == "convert-to-kebab-case"

def test_to_kebab_case_edge_cases():
    assert to_kebab_case("") == ""
    assert to_kebab_case("a") == "a"
    assert to_kebab_case("A") == "a"

def test_to_kebab_case_special_characters():
    assert to_kebab_case("hello@world") == "hello-world"
    assert to_kebab_case("hello world!") == "hello-world"
    assert to_kebab_case("hello---world") == "hello-world"

def test_to_kebab_case_invalid_input():
    with pytest.raises(TypeError):
        to_kebab_case(None)
    with pytest.raises(TypeError):
        to_kebab_case(123)

def test_to_kebab_case_unicode():
    # different behavior for mixed unicode/latin strings vs pure unicode
    assert to_kebab_case("こんにちは World") == "world"
    assert to_kebab_case("Hello-世界") == "hello-世界"
    assert to_kebab_case("こんにちは世界") == "こんにちは-世界"