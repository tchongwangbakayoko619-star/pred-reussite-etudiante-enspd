from pydantic import BaseModel

class DonneesEntree(BaseModel):
    presence_pct: float
    study_min: float
    implication: float
    interaction_ord: float
    acces_bibliotheque_ord: float
