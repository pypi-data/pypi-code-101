from argparse import ArgumentParser

from .cleaner import EXCLUDE_PATTERN, GitBranchCleaner, OVER_DAYS

__all__ = [
    'run',
]


def run() -> None:
    parser = ArgumentParser(description='Git branches cleaner.')
    parser.add_argument(
        '-u',
        '--url',
        help='Git repository remote url.',
    )
    parser.add_argument(
        '-d',
        '--dirpath',
        help='Local dirpath, where git repository is '
             'situated, or where repository should be cloned.',
    )
    parser.add_argument(
        '-o',
        '--over-days',
        default=OVER_DAYS,
        type=int,
        help=f'Number of days, that indicates period, '
             f'where branches will not be deleted, during '
             f'their last commit. Default: {OVER_DAYS}.',
    )
    parser.add_argument(
        '-e',
        '--exclude-pattern',
        default=EXCLUDE_PATTERN,
        help=f'Pattern for search branch names, that will be '
             f'excluded. Default: {EXCLUDE_PATTERN.pattern!r}.',
    )

    args = parser.parse_args()

    GitBranchCleaner(
        repo_url=args.url,
        repo_dirpath=args.dirpath,
        over_days=args.over_days,
        exclude_pattern=args.exclude_pattern,
    ).clean()


if __name__ == '__main__':
    run()
