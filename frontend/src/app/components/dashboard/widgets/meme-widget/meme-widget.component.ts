import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-meme-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './meme-widget.component.html',
  styleUrls: ['./meme-widget.component.scss']
})
export class MemeWidgetComponent implements OnInit {
  @Input() data: string = '';
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;
  currentMemeUrl: string = '';

  private readonly memeUrls: string[] = [
    'https://i.imgflip.com/1g8my4.jpg', // Two Buttons
    'https://i.imgflip.com/3pbbv2.jpg', // Stonks
    'https://i.imgflip.com/1jwhww.jpg', // Distracted Boyfriend
    'https://i.imgflip.com/1iruch.jpg', // This is Fine Dog
    'https://i.imgflip.com/1ur9b0.jpg'  // Drake Hotline Bling
  ];

  ngOnInit(): void {
    this.selectRandomMeme();
  }

  selectRandomMeme(): void {
    const randomIndex = Math.floor(Math.random() * this.memeUrls.length);
    this.currentMemeUrl = this.memeUrls[randomIndex];
  }

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'fun_meme', isPositive });
  }
}

