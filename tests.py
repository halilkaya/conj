#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from unittest import TestCase, main
from conj import conj

class ConjugationTest(TestCase):

    def test_e(self):
        cases = [
            ['piton',   'pitona',     False],
            ['kriko',   'krikoya',    False],
            ['keten',   'ketene',     False],
            ['kurdele', 'kurdeleye',  False],
            ['Burdur',  'Burdur\'a',  True],
            ['İzmir',   'İzmir\'e',   True],
            ['Bolu',    'Bolu\'ya',   True],
            ['Gerede',  'Gerede\'ye', True],
            ['kulak',   'kulağa',     False],
            ['Kulak',   'Kulak\'a',   True],
            ['ben',     'bana',       False],
            ['sen',     'sana',       False],
            ['o',       'ona',        False],
            ['Ben',     'Ben\'e',     True],
            ['Sen',     'Sen\'e',     True],
            ['O',       'O\'ya',      True],
            ['usûl',    'usûle',      False],
            [0,         '0\'a',       False],
            [1,         '1\'e',       False],
            [2,         '2\'ye',      False],
            [3,         '3\'e',       False],
            [4,         '4\'e',       False],
            [5,         '5\'e',       False],
            [6,         '6\'ya',      False],
            [7,         '7\'ye',      False],
            [8,         '8\'e',       False],
            [9,         '9\'a',       False],
            [10,        '10\'a',      False],
            [20,        '20\'ye',     False],
            [30,        '30\'a',      False],
            [40,        '40\'a',      False],
            [50,        '50\'ye',     False],
            [60,        '60\'a',      False],
            [70,        '70\'e',      False],
            [80,        '80\'e',      False],
            [90,        '90\'a',      False],
            [100,       '100\'e',     False],
            [1000,      '1000\'e',    False],
            [1000000,   '1000000\'a', False],
            [1000000000,'1000000000\'a',False],
            [123456789, '123456789\'a', False],
            [1234567890,'1234567890\'a', False],
            [12345678900, '12345678900\'e', False],
            ['123456789','123456789\'a', False]

	]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'e'), case[1])

    def test_i(self):
        cases = [
            ['piton',   'pitonu',     False],
            ['kriko',   'krikoyu',    False],
            ['keten',   'keteni',     False],
            ['kurdele', 'kurdeleyi',  False],
            ['Burdur',  'Burdur\'u',  True],
            ['İzmir',   'İzmir\'i',   True],
            ['Bolu',    'Bolu\'yu',   True],
            ['Gerede',  'Gerede\'yi', True],
            ['Adana',   'Adana\'yı',  True],
            ['kulak',   'kulağı',     False],
            ['Kulak',   'Kulak\'ı',   True],
            ['ben',     'beni',       False],
            ['sen',     'seni',       False],
            ['o',       'onu',        False],
            ['Ben',     'Ben\'i',     True],
            ['Sen',     'Sen\'i',     True],
            ['O',       'O\'yu',      True],
            ['ptn',     'ptn',        False],
            ['usûl',    'usûlü',      False],
            ['mahlûk',  'mahlûğu',    False],
            [0,         '0\'ı',       False],
            [1,         '1\'i',       False],
            [2,         '2\'yi',      False],
            [3,         '3\'ü',       False],
            [4,         '4\'ü',       False],
            [5,         '5\'i',       False],
            [6,         '6\'yı',      False],
            [7,         '7\'yi',      False],
            [8,         '8\'i',       False],
            [9,         '9\'u',       False],
            [10,        '10\'u',      False],
            [20,        '20\'yi',     False],
            [30,        '30\'u',      False],
            [40,        '40\'ı',      False],
            [50,        '50\'yi',     False],
            [60,        '60\'ı',      False],
            [70,        '70\'i',      False],
            [80,        '80\'i',      False],
            [90,        '90\'ı',      False],
            [100,       '100\'ü',     False],
            [1000,      '1000\'i',    False],
            [1000000,   '1000000\'u', False],
            [1000000000,'1000000000\'ı',False],
            [123456789, '123456789\'u', False],
            [1234567890,'1234567890\'ı', False],
            [12345678900,'12345678900\'ü', False],
            ['123456789','123456789\'u', False]
	]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'i'), case[1])

    def test_de(self):
        cases = [
            ['piton',   'pitonda',     False],
            ['kriko',   'krikoda',     False],
            ['keten',   'ketende',     False],
            ['kurdele', 'kurdelede',   False],
            ['Burdur',  'Burdur\'da',  True],
            ['İzmir',   'İzmir\'de',   True],
            ['Bolu',    'Bolu\'da',    True],
            ['Gerede',  'Gerede\'de',  True],
            ['Kulak',   'Kulak\'ta',   True],
            ['ben',     'bende',       False],
            ['sen',     'sende',       False],
            ['o',       'onda',        False],
            ['Ben',     'Ben\'de',     True],
            ['Sen',     'Sen\'de',     True],
            ['O',       'O\'da',       True],
            ['tüf',     'tüfte',       False],
            ['teras',   'terasta',     False],
            ['bilet',   'bilette',     False],
            ['kulak',   'kulakta',     False],
            ['kulaç',   'kulaçta',     False],
            ['savaş',   'savaşta',     False],
            ['seyyah',  'seyyahta',    False],
            ['top',     'topta',       False],
            ['usûl',    'usûlde',      False],
            ['istikbâl','istikbâlde',  False],
	    [0,         '0\'da',       False],
            [1,         '1\'de',       False],
            [2,         '2\'de',       False],
            [3,         '3\'te',       False],
            [4,         '4\'te',       False],
            [5,         '5\'te',       False],
            [6,         '6\'da',       False],
            [7,         '7\'de',       False],
            [8,         '8\'de',       False],
            [9,         '9\'da',       False],
            [10,        '10\'da',      False],
            [20,        '20\'de',      False],
            [30,        '30\'da',      False],
            [40,        '40\'ta',      False],
            [50,        '50\'de',      False],
            [60,        '60\'ta',      False],
            [70,        '70\'te',      False],
            [80,        '80\'de',      False],
            [90,        '90\'da',      False],
            [100,       '100\'de',     False],
            [1000,      '1000\'de',    False],
            [1000000,   '1000000\'da', False],
            [1000000000,'1000000000\'da',False],
            [123456789, '123456789\'da', False],
            [1234567890,'1234567890\'da', False],
            [12345678900, '12345678900\'de', False],
            ['123456789','123456789\'da', False]

	]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'de'), case[1])

    def test_den(self):
        cases = [
            ['piton',   'pitondan',     False],
            ['kriko',   'krikodan',     False],
            ['keten',   'ketenden',     False],
            ['kurdele', 'kurdeleden',   False],
            ['Burdur',  'Burdur\'dan',  True],
            ['İzmir',   'İzmir\'den',   True],
            ['Bolu',    'Bolu\'dan',    True],
            ['Gerede',  'Gerede\'den',  True],
            ['Kulak',   'Kulak\'tan',   True],
            ['ben',     'benden',       False],
            ['sen',     'senden',       False],
            ['o',       'ondan',        False],
            ['Ben',     'Ben\'den',     True],
            ['Sen',     'Sen\'den',     True],
            ['O',       'O\'dan',       True],
            ['tüf',     'tüften',       False],
            ['teras',   'terastan',     False],
            ['bilet',   'biletten',     False],
            ['kulak',   'kulaktan',     False],
            ['kulaç',   'kulaçtan',     False],
            ['savaş',   'savaştan',     False],
            ['seyyah',  'seyyahtan',    False],
            ['top',     'toptan',       False],
            ['usûl',    'usûlden',      False],
            [0,         '0\'dan',       False],
            [1,         '1\'den',       False],
            [2,         '2\'den',       False],
            [3,         '3\'ten',       False],
            [4,         '4\'ten',       False],
            [5,         '5\'ten',       False],
            [6,         '6\'dan',       False],
            [7,         '7\'den',       False],
            [8,         '8\'den',       False],
            [9,         '9\'dan',       False],
            [10,        '10\'dan',      False],
            [20,        '20\'den',      False],
            [30,        '30\'dan',      False],
            [40,        '40\'tan',      False],
            [50,        '50\'den',      False],
            [60,        '60\'tan',      False],
            [70,        '70\'ten',      False],
            [80,        '80\'den',      False],
            [90,        '90\'dan',      False],
            [100,       '100\'den',     False],
            [1000,      '1000\'den',    False],
            [1000000,   '1000000\'dan', False],
            [1000000000,'1000000000\'dan',False],
            [123456789, '123456789\'dan', False],
            [1234567890,'1234567890\'dan', False],
            [12345678900, '12345678900\'den', False],
            ['123456789','123456789\'dan', False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'den'), case[1])

    def test_li(self):
        cases = [
            ['adana',   'Adanalı',      True],
            ['ürgüp',   'Ürgüplü',      True],
            ['bolu',    'Bolulu',       True],
            ['izmir',   'İzmirli',      True],
            ['ığdır',   'Iğdırlı',      True],
            ['usûl',    'usûllü',       False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'li'), case[1])

    def test_siz(self):
        cases = [
            ['piton',   'pitonsuz',     False],
            ['keten',   'ketensiz',     False],
            ['adana',   'Adana\'sız',   True],
            ['ürgüp',   'ürgüpsüz',     False],
            ['usûl',    'usûlsüz',      False],
            ['ahlâk',   'ahlâksız',     False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'siz'), case[1])

    def test_in(self):
        cases = [
            ['piton',   'pitonun',      False],
            ['kriko',   'krikonun',     False],
            ['keten',   'ketenin',      False],
            ['kurdele', 'kurdelenin',   False],
            ['burdur',  'Burdur\'un',   True],
            ['izmir',   'İzmir\'in',    True],
            ['Bolu',    'Bolu\'nun',    True],
            ['gerede',  'Gerede\'nin',  True],
            ['kulak',   'kulağın',      False],
            ['kulak',   'Kulak\'ın',    True],
            ['ben',     'benim',        False],
            ['sen',     'senin',        False],
            ['o',       'onun',         False],
            ['biz',     'bizim',        False],
            ['ben',     'Ben\'in',      True],
            ['sen',     'Sen\'in',      True],
            ['o',       'O\'nun',       True],
            ['biz',     'Biz\'in',      True],
            ['usûl',    'usûlün',       False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'in'), case[1])

    def test_ler(self):
        cases = [
            ['piton',   'pitonlar',     False],
            ['keten',   'ketenler',     False],
            ['burdur',  'Burdur\'lar',  True],
            ['biz',     'bizler',       False],
            ['siz',     'sizler',       False],
            ['o',       'onlar',        False],
            ['o',       'O\'lar',       True],
            ['usûl',    'usûller',      False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'ler'), case[1])

    def test_mek(self):
        cases = [
            ['gez',     'gezmek',       False],
            ['gör',     'görmek',       False],
            ['uç',      'uçmak',        False],
            ['koş',     'koşmak',       False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'mek'), case[1])

if __name__ == '__main__':
    main()
