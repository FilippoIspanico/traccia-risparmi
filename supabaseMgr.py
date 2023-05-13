from supabase import create_client, Client


class SupabaseMgr:
    _url = "https://nexhahnpvmazqtiyeney.supabase.co"

    _key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5leGhhaG5wdm1henF0aXllbmV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODM5ODg1NjIsImV4cCI6MTk5OTU2NDU2Mn0.Wj8In2l_pJ01sBld08vfZJX3wYySPNHE5ZvHSUi9_xU"

    _table = "tabella"

    _columns = ["id", "autore", "risparmi"]

    def __init__(self):
        self.supabase: Client = create_client(self._url, self._key)



    def risparmi_totali(self):
        result = self.supabase.table(self._table).select("*").execute()
        var = result.dict()["data"]
        risparmi_totali = 0
        for elem in var:
            risparmi_totali+= elem["risparmio"]
        return risparmi_totali


    def risparmi_attore(self, autore):
        result = self.supabase.table(self._table).select("*").match({"autore": autore}).execute()
        var = result.dict()["data"]
        risparmi_attore = 0
        for elem in var:
            risparmi_attore += elem["risparmio"]
        return risparmi_attore

    def aggiungi_risparmio(self, autore, risparmio):
        if(autore == "Valeria" or autore == "Filippo"):
            self.supabase.table(self._table).insert({"autore": autore, "risparmio": risparmio}).execute()
            return True
        else:
            return False


# test
# Mgr = SupabaseMgr()
# Mgr.aggiungi_risparmio("Valeria", 100)
# Mgr.aggiungi_risparmio("Filippo", 100)

# print(Mgr.risparmi_totali())

