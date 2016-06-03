import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from obdpi.oled_manager import OledManager


success_list = []
error_list = []


def generate_error():
    error_item = ['test_error', 'This is a test error']
    error_list.append(error_item)


def create_new_oled_manager_test():
    try:
        oled_man = OledManager()
        if oled_man is not None:
            success_item = ['create_new_oled_manager_test']
            success_list.append(success_item)
        else:
            error_item = ['create_new_oled_manager_test', 'Could not create OledManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_oled_manager_test', str(e)]
        error_list.append(error_item)


def run_all():
    create_new_oled_manager_test()

    print_results()


def print_results():
    print 'PASS: {0}'.format(str(len(success_list)))
    print 'FAIL: {0}'.format(str(len(error_list)))
    if len(error_list) > 0:
        for error in error_list:
            print '\t{0}: {1}'.format(str(error[0]), str(error[1]))


run_all()
