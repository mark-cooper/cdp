import sys

class ProgressIndicator(object):

    def __init__(self, total):
        self.count = 0
        self.total = total

    # https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    def tick(self):
        bar_len = 60
        filled_len = int(round(bar_len * self.count / float(self.total)))

        percents = round(100.1 * self.count / float(self.total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ... %s\r' % (bar, percents, '%', f'{self.count}'))
        sys.stdout.flush()
        self.count += 1
