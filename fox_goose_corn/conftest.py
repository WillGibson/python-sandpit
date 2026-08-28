from typeguard import install_import_hook

# Instruments the model with typeguard's runtime type checking at import time, which the
# @typechecked decorator used to do. The decorator confused static analysis: a decorated
# class resolves to the decorator's own type, so every `Boat()` was reported as a call to
# `typechecked` with a missing argument. The hook has the same runtime effect and leaves
# the classes as plain classes.
install_import_hook("fox_goose_corn.src")
