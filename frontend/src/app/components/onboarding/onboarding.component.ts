import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DashboardService } from '../../core/services/dashboard.service';

@Component({
  selector: 'app-onboarding',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './onboarding.component.html',
  styleUrls: ['./onboarding.component.scss']
})
export class OnboardingComponent {
  onboardingForm: FormGroup;
  errorMessage: string | null = null;
  isLoading = false;

  private fb = inject(FormBuilder);
  private dashboardService = inject(DashboardService);
  private router = inject(Router);

  constructor() {
    this.onboardingForm = this.fb.group({
      target_assets: ['', Validators.required],
      investor_persona: ['', Validators.required],
      content_preference: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.onboardingForm.invalid) return;

    this.isLoading = true;
    this.errorMessage = null;

    this.dashboardService.submitOnboarding(this.onboardingForm.value).subscribe({
      next: () => {
        this.isLoading = false;
        this.router.navigate(['/dashboard']);
      },
      error: (err: any) => {
        this.isLoading = false;
        this.errorMessage = err.error?.detail || 'Failed to save preferences. You may have already onboarded.';
        if (err.status === 400 && this.errorMessage?.includes('already exist')) {
          this.router.navigate(['/dashboard']);
        }
      }
    });
  }
}
