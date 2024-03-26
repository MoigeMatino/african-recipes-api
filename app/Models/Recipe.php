<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\MorphMany;

class Recipe extends Model
{
    use HasFactory;

    protected $fillable = [
        'title',
        'description',
        'instructions',
        'prep_time',
        'cook_time',
        'total_time',
        'servings',
        'image_url',
        'ingredients',
        'nutritional_info',
        'premium',
    ];

    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class, 'recipe_tag', 'recipe_id', 'tag_id')->withTimestamps();
    }

    public function likes(): int
    {
        return $this->users_liked()->count();
    }

    public function users_liked(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'likes', 'recipe_id', 'user_id')->withTimestamps();
    }

    public function rating(): float
    {
        return round($this->user_ratings()->get()->avg('pivot.rating'), 1);
    }

    public function user_ratings(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'ratings', 'recipe_id', 'user_id')->withTimestamps()->withPivot('rating');
    }

    public function collaborators(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'collaborators', 'user_id', 'recipe_id')->withTimestamps();
    }

    public function comments(): MorphMany
    {
        return $this->morphMany(Comment::class, 'commentable');
    }
}
