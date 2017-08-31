# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import json
import uvclight

from grokcore.component import name
from nva.psyquizz import hs
from ..quizz2 import Quizz2
from uvclight.auth import require


class Quizz2Charts(uvclight.Page):
    require('manage.company')
    name('charts')
    uvclight.context(Quizz2)

    template = uvclight.get_template('cr.pt', __file__)
    general_stats = None

    def jsonify(self, da):
        return json.dumps(da)

    def update(self, stats, general_stats=None):
        hs.need()
        self.stats = stats
        self.general_stats = general_stats
