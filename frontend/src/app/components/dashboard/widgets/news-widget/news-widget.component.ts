import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

export interface NewsItem {
  id: number;
  title: string;
  url: string;
}

@Component({
  selector: 'app-news-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './news-widget.component.html',
  styleUrls: ['./news-widget.component.scss']
})
export class NewsWidgetComponent {
  @Input() data: NewsItem[] = [];
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'market_news', isPositive });
  }
}