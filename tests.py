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
            [1,         '1\'e',       False],
            [2,         '2\'ye',      False],
            [6,         '6\'ya',      False],
            [0,         '0\'a',       False]
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
            [1,         '1\'i',       False],
            [2,         '2\'yi',      False],
            [3,         '3\'ü',       False],
            [6,         '6\'yı',      False],
            [9,         '9\'u',       False],
            [0,         '0\'ı',       False]
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
            [1,         '1\'de',       False],
            [3,         '3\'te',       False],
            [40,        '40\'ta',      False],
            [0,         '0\'da',       False]
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
            [1,         '1\'den',       False],
            [3,         '3\'ten',       False],
            [40,        '40\'tan',      False],
            [0,         '0\'dan',       False]
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
