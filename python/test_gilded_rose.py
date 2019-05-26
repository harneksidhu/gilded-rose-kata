# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTestRegularItem(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_degradation_within_sell_in(self):
      items = [Item("foo", 4, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(3)]
      self.assertEqual(7,items[0].quality)

    def test_quality_degradation_post_sell_in(self):
      items = [Item("foo", 1, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(3)]
      self.assertEqual(5,items[0].quality)

    def test_quality_not_negative(self):
      items = [Item("foo", 1, 0)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(0,items[0].quality)

    def test_negative_sell_in(self):
      items = [Item("foo", 2, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(6)]
      self.assertEqual(-4,items[0].sell_in)

class GildedRoseTestAgedBrie(unittest.TestCase):
    def test_aged_brie_quality_increase(self):
      items = [Item("Aged Brie", 4, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(11,items[0].quality)

    def test_aged_brie_maximum_quality_increase(self):
      items = [Item("Aged Brie", 4, 49)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(50,items[0].quality)

    def test_aged_brie_quality_post_sell_in(self):
      items = [Item("Aged Brie", 2, 46)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(4)]
      self.assertEqual(50,items[0].quality)

    def test_aged_brie_negative_sell_in(self):
      items = [Item("Aged Brie", 2, 46)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(6)]
      self.assertEqual(-4,items[0].sell_in)

class GildedRoseTestSulfuras(unittest.TestCase):

    item_name = "Sulfuras, Hand of Ragnaros"

    def test_sulfuras_quality_no_change(self):
      items = [Item(self.item_name, 5, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(20,items[0].quality)

    def test_sulfuras_max_quality_no_change(self):
      items = [Item(self.item_name, 5, 80)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(80,items[0].quality)

    def test_sulfuras_no_sell_in_change(self):
      items = [Item(self.item_name, 5, 80)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(5,items[0].sell_in)

class GildedRoseTestBacktage(unittest.TestCase):

    item_name = "Backstage passes to a TAFKAL80ETC concert"

    def test_backstage_quality_increase_sell_in_gt_10_days(self):
      items = [Item(self.item_name, 11, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(21,items[0].quality)

    def test_backstage_quality_increase_sell_in_lt_10_days(self):
      items = [Item(self.item_name, 10, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(22,items[0].quality)

    def test_backstage_quality_increase_sell_in_lt_5_days(self):
      items = [Item(self.item_name, 5, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(23,items[0].quality)

    def test_backstage_quality_post_sell_in(self):
      items = [Item(self.item_name, 1, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(0,items[0].quality)

    def test_backstage_negative_sell_in(self):
      items = [Item(self.item_name, 2, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(6)]
      self.assertEqual(-4,items[0].sell_in)

class GildedRoseTestConjure(unittest.TestCase):

    item_name = "Conjured"

    def test_conjured_quality_degradation_within_sell_in(self):
      items = [Item(self.item_name, 1, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(1)]
      self.assertEqual(18,items[0].quality)

    def test_conjured_quality_degradation_post_sell_in(self):
      items = [Item(self.item_name, 1, 20)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(2)]
      self.assertEqual(14,items[0].quality)

    def test_conjured_negative_sell_in(self):
      items = [Item(self.item_name, 2, 10)]
      gilded_rose = GildedRose(items)
      [gilded_rose.update_quality() for _ in range(6)]
      self.assertEqual(-4,items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
