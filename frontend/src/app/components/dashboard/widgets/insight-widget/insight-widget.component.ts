import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-insight-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './insight-widget.component.html',
  styleUrls: ['./insight-widget.component.scss']
})
export class InsightWidgetComponent {
  @Input() data: string = '';
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'ai_insight', isPositive });
  }
}