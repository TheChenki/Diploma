import keras
import os
from flask import current_app as app
from forms.HouseForm import HouseForm
import pandas as pd
import numpy as np
import joblib


class HousePricePredictor:
    PRICE_COEFFICIENT = 6282996.531418986

    def __init__(self, form: HouseForm):
        self._load_model()
        self._to_dataframe(form)
        self._preprocess_data()

    def predict(self):
        price = self.model.predict(self.data) * self.PRICE_COEFFICIENT
        return price.flatten() if price > 0 else [0]

    def _load_model(self):
        model_path = os.path.join(app.root_path, 'nn_models', 'model_3_m')
        self.model = keras.models.load_model(model_path)

    def _to_dataframe(self, form: HouseForm):
        self.data = pd.DataFrame()
        self.data['LotFrontage'] = [form.lot_frontage.data]
        self.data['LotArea'] = [form.lot_area.data]
        self.data['Street'] = [form.street.data]
        self.data['Alley'] = [form.alley.data]
        self.data['LotShape'] = [form.lot_shape.data]
        self.data['LandContour'] = [form.land_contour.data]
        self.data['Utilities'] = [form.utilities.data]
        self.data['LotConfig'] = [form.lot_config.data]
        self.data['LandSlope'] = [form.land_slope.data]
        self.data['Neighborhood'] = [form.neighborhood.data]
        self.data['BldgType'] = [form.building_type.data]
        self.data['HouseStyle'] = [form.house_style.data]
        self.data['OverallQual'] = [form.overall_quality.data]
        self.data['OverallCond'] = [form.overall_condition.data]
        self.data['YearBuilt'] = [form.year_build.data]
        self.data['YearRemodAdd'] = [form.year_remodel.data]
        self.data['RoofStyle'] = [form.roof_style.data]
        self.data['RoofMatl'] = [form.roof_material.data]
        self.data['Exterior1st'] = [form.exterior_first.data]
        self.data['Exterior2nd'] = [form.exterior_second.data]
        self.data['MasVnrType'] = [form.masonry_veneer_type.data]
        self.data['MasVnrArea'] = [form.masonry_veneer_area.data]
        self.data['ExterQual'] = [form.exterior_quality.data]
        self.data['ExterCond'] = [form.exterior_condition.data]
        self.data['Foundation'] = [form.foundation.data]
        self.data['BsmtQual'] = [form.basement_quality.data]
        self.data['BsmtCond'] = [form.basement_condition.data]
        self.data['BsmtExposure'] = [form.basement_exposure.data]
        self.data['BsmtFinType1'] = [form.basement_type_1.data]
        self.data['BsmtFinSF1'] = [form.basement_finished_area_1.data]
        self.data['BsmtFinType2'] = [form.basement_type_2.data]
        self.data['BsmtFinSF2'] = [form.basement_finished_area_2.data]
        self.data['BsmtUnfSF'] = [form.basement_unfinished_area.data]
        self.data['TotalBsmtSF'] = [form.basement_finished_area_1.data + form.basement_finished_area_2.data + form.basement_unfinished_area.data]
        self.data['Heating'] = [form.heating_type.data]
        self.data['HeatingQC'] = [form.heating_quality.data]
        self.data['CentralAir'] = [form.central_air.data]
        self.data['Electrical'] = [form.electrical.data]
        self.data['1stFlrSF'] = [form.first_floor_area.data]
        self.data['2ndFlrSF'] = [form.second_floor_area.data]
        self.data['LowQualFinSF'] = [form.lq_finished_area.data]
        self.data['GrLivArea'] = [form.first_floor_area.data + form.second_floor_area.data + form.lq_finished_area.data]
        self.data['BsmtFullBath'] = [form.basement_full_bath.data]
        self.data['BsmtHalfBath'] = [form.basement_half_bath.data]
        self.data['FullBath'] = [form.full_bath.data]
        self.data['HalfBath'] = [form.half_bath.data]
        self.data['BedroomAbvGr'] = [form.bedrooms.data]
        self.data['KitchenAbvGr'] = [form.kitchens.data]
        self.data['KitchenQual'] = [form.kitchen_quality.data]
        self.data['TotRmsAbvGrd'] = [form.total_rooms.data]
        self.data['Functional'] = [form.functionality.data]
        self.data['Fireplaces'] = [form.fireplaces.data]
        self.data['FireplaceQu'] = [form.fireplace_quality.data]
        self.data['GarageType'] = [form.garage_type.data]
        self.data['GarageYrBlt'] = [form.garage_year.data]
        self.data['GarageFinish'] = [form.garage_finish.data]
        self.data['GarageCars'] = [form.garage_cars.data]
        self.data['GarageArea'] = [form.garage_area.data]
        self.data['GarageQual'] = [form.garage_quality.data]
        self.data['GarageCond'] = [form.garage_condition.data]
        self.data['PavedDrive'] = [form.paved_drive.data]
        self.data['WoodDeckSF'] = [form.wood_deck_area.data]
        self.data['OpenPorchSF'] = [form.open_porch_area.data]
        self.data['EnclosedPorch'] = [form.enclosed_porch.data]
        self.data['3SsnPorch'] = [form.three_season_porch_area.data]
        self.data['ScreenPorch'] = [form.screen_porch_area.data]
        self.data['PoolArea'] = [form.pool_area.data]
        self.data['PoolQC'] = [form.pool_quality.data]
        self.data['Fence'] = [form.fence.data]
        self.data['MiscFeature'] = [form.misc_feature.data]
        self.data['MiscVal'] = [form.misc_value.data]

    def _preprocess_data(self):
        scaler_path = os.path.join(app.root_path, 'nn_models', 'scaler_updated.save')
        scaler = joblib.load(scaler_path)

        matrix = np.matrix(self.data)

        col_names = self.data.keys()
        self.data = pd.DataFrame(scaler.transform(matrix), columns=col_names)
