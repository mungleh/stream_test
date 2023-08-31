import pytest
import pandas as pd
from pages.find_ville import get_ville, select_ville

#test si un df c un df
def test_get_ville():
    assert isinstance(get_ville, pd.DataFrame)

#test si un str c un str ( et le bon)
def test_select_ville():
    my_var = 'belleville'
    assert type(my_var) is str
    assert select_ville("belleville") == 'belleville'
