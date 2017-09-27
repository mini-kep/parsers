# -*- coding: utf-8 -*-
import datetime
import pytest

from helpers import DateHelper

class Test_today:
    def test_today(self):
        assert DateHelper.today() == datetime.date.today()

class Test_make_date:
    def test_make_date_on_valid_input(self):
        date = DateHelper.make_date('2007-01-25')
        assert date.day == 25
        assert date.month == 1
        assert date.year == 2007

    def test_make_date_on_valid_input_in_slashed_format(self):
        date = DateHelper.make_date('2007/01/25')
        assert date.day == 25
        assert date.month == 1
        assert date.year == 2007

    def test_make_date_on_valid_input_none(self):
        assert DateHelper.make_date(None) == datetime.date.today()

    def test_make_date_on_invalid_input_out_of_range(self):
        with pytest.raises(ValueError):
            DateHelper.make_date('2007-25-01')

    def test_make_date_on_invalid_input_empty_str_raises_exception(self):
        with pytest.raises(Exception):
            DateHelper.make_date('')

    def test_make_date_on_no_argument_empty_raises_type_error(self):
        with pytest.raises(TypeError):
            DateHelper.make_date()

class Test_get_end:
    def test_on_none_argument_returns_today(self):
        assert DateHelper.get_end(None) == datetime.date.today()

class Test_get_start:
    def test_on_none_argument_returns_date(self):
        date = datetime.date(3020,1,25)
        assert DateHelper.get_start(None,date) == date

class Test_to_date:
    def test_on_valid_format_day_month_year(self):
        assert DateHelper.to_date('13-02-1254','%d-%m-%Y') == '1254-02-13'
    def test_on_invalid_format(self):
        with pytest.raises(Exception):
            assert DateHelper.to_date('13-02-1254','%dk%m-%Y') == '1254-02-13'


