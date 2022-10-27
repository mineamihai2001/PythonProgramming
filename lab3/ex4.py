def build_xml_element(tag, content, **name_parameters):
    output = "<" + tag
    for key_value in name_parameters:
        output += " " + key_value + "=" + name_parameters[key_value]
    output = output + ">" + content + "</" + tag + ">"
    return output


print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
