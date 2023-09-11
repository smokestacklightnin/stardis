class StellarModel:
    """
    Class containing information about the stellar model.

    Parameters
    ----------
    temperatures : numpy.ndarray
    geometry : stardis.model.geometry
    composition : stardis.model.composition.base.Composition

    Attributes
    ----------
    temperatures : numpy.ndarray
        Temperatures in K of all depth points. Note that array is transposed.
    geometry : stardis.model.geometry
        Geometry of the model.
    composition : stardis.model.composition.base.Composition
        Composition of the model. Includes density and atomic mass fractions.
    """

    def __init__(self, temperatures, geometry, composition):
        self.temperatures = temperatures
        self.geometry = geometry
        self.composition = composition
