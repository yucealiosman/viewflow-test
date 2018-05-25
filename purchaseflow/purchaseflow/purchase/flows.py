from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import UpdateProcessView
from viewflow.lock import select_for_update_lock

from . import view
from .models import LeaveProcess, LeaveTask


@frontend.register
class LeaveFlow(Flow):
    """

    Leave Workflow
    """
    process_class = LeaveProcess
    task_class = LeaveTask
    lock_impl = select_for_update_lock

    summary_template = """
        Leave Form For Gozen Hold.
        """

    start = (
        flow.Start(view.StartView)
        .Permission('leave.can_create_leave')
        .Next(this.split_clerk_warehouse)
    )


    end = flow.End()
