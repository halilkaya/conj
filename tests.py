#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from unittest import TestCase, main
from conj import conj

class ConjugationTest(TestCase):

    def test_dative(self):
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
            ['O',       'O\'ya',      True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'dative'), case[1])

    def test_accusative(self):
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
            ['O',       'O\'yu',      True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'accusative'), case[1])

    def test_adessive(self):
        cases = [
            ['piton',   'pitonda',     False],
            ['kriko',   'krikoda',     False],
            ['keten',   'ketende',     False],
            ['kurdele', 'kurdelede',   False],
            ['Burdur',  'Burdur\'da',  True],
            ['İzmir',   'İzmir\'de',   True],
            ['Bolu',    'Bolu\'da',    True],
            ['Gerede',  'Gerede\'de',  True],
            ['kulak',   'kulakta',     False],
            ['Kulak',   'Kulak\'ta',   True],
            ['ben',     'bende',       False],
            ['sen',     'sende',       False],
            ['o',       'onda',        False],
            ['Ben',     'Ben\'de',     True],
            ['Sen',     'Sen\'de',     True],
            ['O',       'O\'da',       True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'adessive'), case[1])

    def test_ablative(self):
        cases = [
            ['piton',   'pitondan',     False],
            ['kriko',   'krikodan',     False],
            ['keten',   'ketenden',     False],
            ['kurdele', 'kurdeleden',   False],
            ['Burdur',  'Burdur\'dan',  True],
            ['İzmir',   'İzmir\'den',   True],
            ['Bolu',    'Bolu\'dan',    True],
            ['Gerede',  'Gerede\'den',  True],
            ['kulak',   'kulaktan',     False],
            ['Kulak',   'Kulak\'tan',   True],
            ['ben',     'benden',       False],
            ['sen',     'senden',       False],
            ['o',       'ondan',        False],
            ['Ben',     'Ben\'den',     True],
            ['Sen',     'Sen\'den',     True],
            ['O',       'O\'dan',       True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'ablative'), case[1])

    def test_derivative(self):
        cases = [
            ['adana',   'Adanalı',      True],
            ['ürgüp',   'Ürgüplü',      True],
            ['bolu',    'Bolulu',       True],
            ['izmir',   'İzmirli',      True],
            ['ığdır',   'Iğdırlı',      True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'derivative'), case[1])

    def test_abesive(self):
        cases = [
            ['piton',   'pitonsuz',     False],
            ['keten',   'ketensiz',     False],
            ['adana',   'Adana\'sız',   True],
            ['ürgüp',   'ürgüpsüz',     False]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'abesive'), case[1])

    def test_genitive(self):
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
            ['biz',     'Biz\'in',      True]
        ]

        for case in cases:
            self.assertEqual(conj(case[0], case[2], 'genitive'), case[1])

if __name__ == '__main__':
    main()
