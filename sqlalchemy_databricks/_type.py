from pyhive.sqlalchemy_hive import HiveTypeCompiler


class DatabricksTypeCompiler(HiveTypeCompiler):
    def visit_DATE(self, type_):
        # Woraround because pyhive uses TIMESTAMP instead of DATE.
        # See as well: https://github.com/dropbox/PyHive/issues/139
        return 'DATE'
