import sys
import getopt


def get_start_and_end_dates():
    start_date = None
    end_date = None

    argv = sys.argv[1:]
    # print(argv)
    try:
        opts, args = getopt.getopt(argv, "s:e:", ["start_date=", "end_date="])
    except getopt.GetoptError as err:
        print(err)
        opts = []
    # print(opts)

    for opt, arg in opts:
        if opt in ['-s', '--start_date']:
            start_date = arg
        elif opt in ['-e', '--end_date']:
            end_date = arg

    print(f'start_date: {start_date}')
    print(f'end_date: {end_date}')


get_start_and_end_dates()