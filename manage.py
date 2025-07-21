#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BruBox.settings')
  # تأكد من استخدام الحروف الكبيرة والصحيحة

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "تعذر استيراد Django. تأكد من أنه مثبت في بيئة العمل الافتراضية "
            "وأنك قمت بتفعيل البيئة الافتراضية (venv)."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
