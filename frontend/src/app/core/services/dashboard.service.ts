import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

export interface UserPreferences {
  target_assets: string;
  investor_persona: string;
  content_preference: string;
}

export interface DashboardData {
  prices: any;
  news: any[];
  insight: string;
  meme: string;
  preferences: UserPreferences;
}

export interface FeedbackData {
  widget_type: string;
  is_positive: boolean;
  interaction_context?: string;
}

@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  private http = inject(HttpClient);
  private apiUrl = environment.apiUrl;

  submitOnboarding(preferences: UserPreferences): Observable<any> {
    return this.http.post(`${this.apiUrl}/onboarding`, preferences);
  }

  getDashboardData(): Observable<DashboardData> {
    return this.http.get<DashboardData>(`${this.apiUrl}/dashboard`);
  }

  submitFeedback(widgetType: string, isPositive: boolean, context?: string): Observable<any> {
    const payload: FeedbackData = {
      widget_type: widgetType,
      is_positive: isPositive
    };
    if (context) {
      payload.interaction_context = context;
    }
    return this.http.post(`${this.apiUrl}/feedback`, payload);
  }
}
