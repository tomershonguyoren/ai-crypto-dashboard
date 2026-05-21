import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-meme-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './meme-widget.component.html',
  styleUrls: ['./meme-widget.component.scss']
})
export class MemeWidgetComponent {
  @Input() data: string = '';
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'fun_meme', isPositive });
  }
}