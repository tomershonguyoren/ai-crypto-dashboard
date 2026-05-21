import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-prices-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './prices-widget.component.html',
  styleUrls: ['./prices-widget.component.scss']
})
export class PricesWidgetComponent {
  Math = Math; // Make Math available to template
  @Input() data: { [key: string]: { usd: number, usd_24h_change: number } } = {};
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'coin_prices', isPositive });
  }
}