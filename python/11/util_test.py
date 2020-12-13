import filecmp
import unittest
import util

class UtilTest(unittest.TestCase):

  def one_reseat_pass(self, path1, path2):
    out_path = 'expected_' + path2
    with open(path1) as in_file, open(out_path, 'w') as out_file:
      for l in util.reseat(in_file):
        out_file.write(l)
    self.assertTrue(filecmp.cmp(path2, out_path, shallow=False), 'Files differ: ' + path2 + ', ' + out_path)

  def test_reseat_part_1(self):
    file_list = (
      'test_input_1.txt',
      'test_input_2.txt',
      'test_input_3.txt',
      'test_input_4.txt',
      'test_input_5.txt',
      'test_input_6.txt'
    )
    for i in range(len(file_list) - 1):
      self.one_reseat_pass(file_list[i], file_list[i+1])
    self.one_reseat_pass(file_list[-1], file_list[-1])

  def one_reseat_pass_part_2(self, path1, path2):
    out_path = 'expected_' + path2
    with open(path1) as in_file, open(out_path, 'w') as out_file:
      for l in util.reseat_part_2(in_file):
        out_file.write(l)
    self.assertTrue(filecmp.cmp(path2, out_path, shallow=False), 'Files differ: ' + path2 + ', ' + out_path)

  def test_reseat_part_2(self):
    file_list = (
      'part_2_input_1.txt',
      'part_2_input_2.txt',
      'part_2_input_3.txt',
      'part_2_input_4.txt',
      'part_2_input_5.txt',
      'part_2_input_6.txt',
      'part_2_input_7.txt'
    )
    for i in range(len(file_list) - 1):
      self.one_reseat_pass_part_2(file_list[i], file_list[i+1])
    self.one_reseat_pass_part_2(file_list[-1], file_list[-1])


if __name__ == '__main__':
    unittest.main()
