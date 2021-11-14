import libcreator
new_lib = libcreator.Library()
new_lib.get_information()       # this guides you throu the creation.
new_lib.fill_in_information()   # this formats the gathered informatin
new_lib.create_library()        # this writes the new library directory
print("Now fill the " + new_lib.package_path + new_lib.library_name + ".py" + " with your modules and press enter to compile")
input("Waiting...")
new_lib.compile_library()       # this compiles teh directory to and .whl