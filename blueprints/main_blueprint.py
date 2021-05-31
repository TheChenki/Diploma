from flask import Blueprint, render_template

from forms.HouseForm import HouseForm
from classes.HousePricePredictor import HousePricePredictor

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = HouseForm()

    if form.validate_on_submit():
        predictor = HousePricePredictor(form)
        price = predictor.predict()
        return render_template('index.html', form=form, price=str(price[0]))

    return render_template('index.html', form=form)
