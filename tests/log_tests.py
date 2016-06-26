import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from obdpi.log_manager import LogManager


success_list = []
error_list = []


def generate_error():
    error_item = ['test', 'This is a test error']
    error_list.append(error_item)


def create_new_log_manager_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            success_item = 'create_new_log_manager_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_test', str(e)]
        error_list.append(error_item)


def create_new_log_manager_add_info_entry_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            log_man.add_info_entry_to_log('Test INFO entry')
            success_item = 'create_new_log_manager_add_info_entry_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_add_info_entry_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_add_info_entry_test', str(e)]
        error_list.append(error_item)


def create_new_log_manager_add_debug_entry_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            log_man.add_debug_entry_to_log('Test DEBUG entry')
            success_item = 'create_new_log_manager_add_debug_entry_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_add_debug_entry_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_add_debug_entry_test', str(e)]
        error_list.append(error_item)


def create_new_log_manager_add_warning_entry_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            log_man.add_warning_entry_to_log('Test WARNING entry')
            success_item = 'create_new_log_manager_add_warning_entry_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_add_warning_entry_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_add_warning_entry_test', str(e)]
        error_list.append(error_item)


def create_new_log_manager_get_log_count_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            log_count = log_man.get_log_count()
            success_item = 'create_new_log_manager_get_log_count_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_get_log_count_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_get_log_count_test', str(e)]
        error_item.append(error_item)


def create_new_log_manager_get_oldest_log_file_name_test():
    try:
        log_man = LogManager('tests/')
        if log_man is not None:
            oldest_log_file_name = log_man.get_oldest_log_file_name()
            success_item = 'create_new_log_manager_get_oldest_log_file_name_test'
            success_list.append(success_item)
        else:
            error_item = ['create_new_log_manager_get_oldest_log_file_name_test', 'Could not create LogManager object']
            error_list.append(error_item)
    except Exception, e:
        error_item = ['create_new_log_manager_get_oldest_log_file_name_test', str(e)]
        error_item.append(error_item)


def run_all():
    create_new_log_manager_test()
    create_new_log_manager_add_info_entry_test()
    create_new_log_manager_add_debug_entry_test()
    create_new_log_manager_add_warning_entry_test()
    create_new_log_manager_get_log_count_test()
    create_new_log_manager_get_oldest_log_file_name_test()

    print_results()


def print_results():
    print 'PASS: {0}'.format(str(len(success_list)))
    print 'FAIL: {0}'.format(str(len(error_list)))
    if len(error_list) > 0:
        for error in error_list:
            print '\t{0}: {1}'.format(str(error[0]), str(error[1]))


run_all()

