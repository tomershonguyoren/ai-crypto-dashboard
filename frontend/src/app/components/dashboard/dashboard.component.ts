import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardService, DashboardData } from '../../core/services/dashboard.service';
import { NewsWidgetComponent } from './widgets/news-widget/news-widget.component';
import { PricesWidgetComponent } from './widgets/prices-widget/prices-widget.component';
import { InsightWidgetComponent } from './widgets/insight-widget/insight-widget.component';
import { MemeWidgetComponent } from './widgets/meme-widget/meme-widget.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule, 
    NewsWidgetComponent, 
    PricesWidgetComponent, 
    InsightWidgetComponent, 
    MemeWidgetComponent
  ],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  isLoading = true;
  dashboardData!: DashboardData;

  private dashboardService = inject(DashboardService);

  ngOnInit(): void {
    this.dashboardService.getDashboardData().subscribe({
      next: (data) => {
        this.dashboardData = data;
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Failed to fetch dashboard data', err);
        this.isLoading = false;
      }
    });
  }

  handleFeedback(event: { widgetType: string, isPositive: boolean }): void {
    this.dashboardService.submitFeedback(event.widgetType, event.isPositive).subscribe({
      next: () => console.log(`Feedback saved for ${event.widgetType}`),
      error: (err) => console.error('Failed to submit feedback', err)
    });
  }
}
