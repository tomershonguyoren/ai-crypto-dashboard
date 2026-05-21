import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.scss']
})
export class AuthComponent {
  isLoginMode = true;
  authForm: FormGroup;
  errorMessage: string | null = null;
  isLoading = false;

  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);

  constructor() {
    this.authForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      name: [''] // Optional for login, required dynamically
    });
  }

  toggleMode() {
    this.isLoginMode = !this.isLoginMode;
    this.errorMessage = null;
    if (!this.isLoginMode) {
      this.authForm.get('name')?.setValidators([Validators.required]);
    } else {
      this.authForm.get('name')?.clearValidators();
    }
    this.authForm.get('name')?.updateValueAndValidity();
    this.authForm.reset();
  }

  onSubmit() {
    if (this.authForm.invalid) return;

    this.isLoading = true;
    this.errorMessage = null;
    const formData = this.authForm.value;

    if (this.isLoginMode) {
      this.authService.login({ email: formData.email, password: formData.password }).subscribe({
        next: () => {
          this.isLoading = false;
          this.router.navigate(['/dashboard']);
        },
        error: (err) => {
          this.isLoading = false;
          this.errorMessage = err.error?.detail || 'Invalid email or password.';
        }
      });
    } else {
      this.authService.signup(formData).subscribe({
        next: () => {
          // Immediately log them in after signup
          this.authService.login({ email: formData.email, password: formData.password }).subscribe({
            next: () => {
              this.isLoading = false;
              this.router.navigate(['/onboarding']);
            },
            error: () => {
              this.isLoading = false;
              this.router.navigate(['/auth']); // Fallback
            }
          });
        },
        error: (err) => {
          this.isLoading = false;
          this.errorMessage = err.error?.detail || 'Email already exists or invalid data.';
        }
      });
    }
  }
}
